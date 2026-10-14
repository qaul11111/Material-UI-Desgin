"""Small, deterministic, read-only helpers for Material handoff QA."""
import hashlib
import json
from pathlib import Path


def read_json(path):
    def reject_constant(value):
        raise ValueError("Non-finite JSON number: " + value)
    return json.loads(Path(path).read_text(encoding="utf-8"),
                      parse_constant=reject_constant)


def finding(rule, location, message, status="fail"):
    return dict(ruleId=rule, location=str(location), status=status, evidence=message)


def report(findings, scope):
    findings = sorted(findings, key=lambda x: (x["location"], x["ruleId"], x["evidence"]))
    status = ("failed" if any(x["status"] == "fail" for x in findings) else
              "needs-review" if any(x["status"] == "review" for x in findings)
              else "checks-clear")
    return dict(status=status, scope=scope, findings=findings,
                limitation="Checks-clear is not proof of visual, semantic or Material compliance.")


def emit(result, output_format="json"):
    if output_format == "markdown":
        print("# QA: " + result["status"] + "\n")
        print(result["scope"] + "\n")
        for item in result["findings"]:
            # Keep untrusted node names as text, not HTML/directives.
            value = json.dumps(item, ensure_ascii=False).replace("<", "&lt;")
            print("- " + value)
        print("\n" + result["limitation"])
        if result.get("manualChecks"):
            print("\n## Manual checks still required\n")
            for item in result["manualChecks"]:
                print("- " + item)
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return {"checks-clear": 0, "failed": 1, "needs-review": 2}[result["status"]]


def local_file(root, value):
    """Never escape the user-specified handoff directory or fetch remote URLs."""
    if not isinstance(value, str) or not value or "://" in value:
        raise ValueError("A nonempty local handoff-relative path is required")
    relative = Path(value)
    if relative.is_absolute():
        raise ValueError("Absolute artifact paths are not accepted")
    root = Path(root).resolve()
    path = (root / relative).resolve()
    try:
        path.relative_to(root)
    except ValueError:
        raise ValueError("Artifact path escapes handoff root")
    if not path.is_file():
        raise ValueError("Artifact file is missing: " + value)
    return path


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()
