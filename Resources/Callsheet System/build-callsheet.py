#!/usr/bin/env python3
"""
Build a self-contained callsheet HTML page.

Inlines every reference image as a base64 data: URI so the finished page needs
no network at all — it renders on a phone in airplane mode, which is the whole
point on a shoot.

Usage
-----
    python3 build-callsheet.py <filled-template.html> <images-dir> <output.html>

The template must contain __IMG_<NAME>__ tokens. For each one, the script looks
for <images-dir>/<NAME>.jpg and swaps the token for the encoded image.

Prepare images first (macOS, no extra installs required):

    sips -s format jpeg -s formatOptions 62 -Z 460 raw.jpg --out images/R1.jpg

460px on the long edge at quality 62 lands each reference around 40 KB, which
keeps a 16-image board under 1 MB. Artifacts cap at 16 MB total.
"""
import base64
import pathlib
import re
import sys


def main() -> int:
    if len(sys.argv) != 4:
        print(__doc__)
        return 2

    template = pathlib.Path(sys.argv[1])
    imgdir = pathlib.Path(sys.argv[2])
    out = pathlib.Path(sys.argv[3])

    if not template.exists():
        print(f"error: template not found: {template}")
        return 1

    html = template.read_text(encoding="utf-8")

    unfilled = sorted(set(re.findall(r"\{\{([A-Z0-9_]+)\}\}", html)))
    if unfilled:
        print(f"warning: {len(unfilled)} unfilled {{{{TOKENS}}}} remain: {', '.join(unfilled[:8])}"
              + (" ..." if len(unfilled) > 8 else ""))

    tokens = sorted(set(re.findall(r"__IMG_([A-Z0-9]+)__", html)))
    if not tokens:
        print("note: no __IMG_*__ tokens — writing through with no images")

    missing = [t for t in tokens if not (imgdir / f"{t}.jpg").exists()]
    if missing:
        print(f"error: missing images in {imgdir}: {', '.join(missing)}")
        return 1

    for token in tokens:
        raw = (imgdir / f"{token}.jpg").read_bytes()
        uri = "data:image/jpeg;base64," + base64.b64encode(raw).decode("ascii")
        html = html.replace(f"__IMG_{token}__", uri)

    leftover = re.findall(r"__IMG_[A-Z0-9]+__", html)
    if leftover:
        print(f"error: unreplaced image tokens: {sorted(set(leftover))}")
        return 1

    # the checklist tally is rendered from the DOM at runtime, so no count to patch
    out.write_text(html, encoding="utf-8")
    size = out.stat().st_size
    print(f"embedded {len(tokens)} images: {', '.join(tokens) if tokens else '(none)'}")
    print(f"wrote {out} — {size/1024:.0f} KB ({size/1024/1024:.2f} MB of the 16 MB artifact budget)")

    if size > 15 * 1024 * 1024:
        print("WARNING: over 15 MB — downscale the images before publishing")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
