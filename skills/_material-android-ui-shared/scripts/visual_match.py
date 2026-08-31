#!/usr/bin/env python3
"""Deterministic pixel-match check for Material UI reference screenshots."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Iterable, NoReturn, TypeVar

try:
    from PIL import Image, ImageChops
except ImportError as exc:  # pragma: no cover - environment diagnostic
    raise SystemExit("Pillow is required: install it in the task environment") from exc


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Compare equal-size screenshots. A pixel passes when the maximum "
            "RGBA channel difference is within the configured tolerance."
        )
    )
    parser.add_argument("reference", type=Path)
    parser.add_argument("actual", type=Path)
    parser.add_argument("--threshold", type=float, default=0.99)
    parser.add_argument("--channel-tolerance", type=int, default=8)
    parser.add_argument(
        "--mask",
        type=Path,
        help="Optional equal-size grayscale/RGBA image; pixels above 127 are excluded.",
    )
    parser.add_argument("--diff-out", type=Path)
    parser.add_argument("--json-out", type=Path)
    return parser.parse_args()


Pixel = TypeVar("Pixel")


def flattened_pixels(image: Image.Image) -> Iterable[Pixel]:
    """Use Pillow's non-deprecated iterator while retaining older compatibility."""
    getter = getattr(image, "get_flattened_data", None)
    return getter() if getter else image.getdata()


def fail_input(message: str) -> NoReturn:
    print(json.dumps({"status": "error", "message": message}), file=sys.stderr)
    raise SystemExit(2)


def main() -> int:
    args = parse_args()
    if not 0 <= args.threshold <= 1:
        fail_input("--threshold must be between 0 and 1")
    if not 0 <= args.channel_tolerance <= 255:
        fail_input("--channel-tolerance must be between 0 and 255")

    try:
        reference = Image.open(args.reference).convert("RGBA")
        actual = Image.open(args.actual).convert("RGBA")
    except (OSError, ValueError) as exc:
        fail_input(f"unable to read screenshot: {exc}")

    if reference.size != actual.size:
        fail_input(
            f"dimension mismatch: reference={reference.size}, actual={actual.size}; "
            "resizing is intentionally forbidden"
        )

    excluded: list[bool]
    if args.mask:
        try:
            mask = Image.open(args.mask).convert("L")
        except (OSError, ValueError) as exc:
            fail_input(f"unable to read mask: {exc}")
        if mask.size != reference.size:
            fail_input(f"mask dimension mismatch: mask={mask.size}, screenshot={reference.size}")
        excluded = [value > 127 for value in flattened_pixels(mask)]
    else:
        excluded = [False] * (reference.width * reference.height)

    difference = ImageChops.difference(reference, actual)
    channel_differences = list(flattened_pixels(difference))
    evaluated = 0
    passed = 0
    failed = 0
    max_difference = 0
    heatmap_pixels: list[tuple[int, int, int, int]] = []

    for channels, is_excluded in zip(channel_differences, excluded):
        if is_excluded:
            heatmap_pixels.append((0, 0, 0, 0))
            continue
        evaluated += 1
        pixel_max = max(channels)
        max_difference = max(max_difference, pixel_max)
        if pixel_max <= args.channel_tolerance:
            passed += 1
            heatmap_pixels.append((0, 0, 0, 255))
        else:
            failed += 1
            heatmap_pixels.append((max(64, pixel_max), 0, 0, 255))

    if evaluated == 0:
        fail_input("mask excludes every pixel")

    score = passed / evaluated
    result = {
        "status": "passed" if score >= args.threshold else "failed",
        "reference": str(args.reference),
        "actual": str(args.actual),
        "width": reference.width,
        "height": reference.height,
        "threshold": args.threshold,
        "channelTolerance": args.channel_tolerance,
        "evaluatedPixels": evaluated,
        "excludedPixels": len(excluded) - evaluated,
        "passedPixels": passed,
        "failedPixels": failed,
        "matchRatio": round(score, 8),
        "maxChannelDifference": max_difference,
    }

    if args.diff_out:
        args.diff_out.parent.mkdir(parents=True, exist_ok=True)
        heatmap = Image.new("RGBA", reference.size)
        heatmap.putdata(heatmap_pixels)
        heatmap.save(args.diff_out)
        result["diff"] = str(args.diff_out)

    rendered = json.dumps(result, ensure_ascii=False, indent=2)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0 if score >= args.threshold else 1


if __name__ == "__main__":
    raise SystemExit(main())
