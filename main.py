"""Publish the 19 November 2026 front page as the competition entry image.

The finished page sits next to this script as entry.png: a newspaper
front page for Thursday 19 November 2026, built from that day's news.
This script does nothing creative — it checks the vendored file is the
exact page it should be, then places an identical copy at the path the
grader reads. Standard library only, no network, no third-party code.
"""

from hashlib import file_digest
from os import environ
from pathlib import Path

PAGE = Path(__file__).resolve().parent / "entry.png"
# sha256 of the composed 19 November 2026 front page; the copy is
# verified against it so a corrupted or swapped vendored file fails
# loudly instead of entering the wrong image.
EXPECTED_DIGEST = "5197959aab5ee48a228f9a722727edd45b710a67a616a618912bd2af381bf1f1"
SIZE_LIMIT = 1024 * 1024
EDGE_LIMIT = 1024
PNG_SIGNATURE = bytes((0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A))


def digest_of(path):
    with path.open("rb") as handle:
        return file_digest(handle, "sha256").hexdigest()


def dimensions_of(path):
    blob = path.read_bytes()
    if blob[:8] != PNG_SIGNATURE:
        raise ValueError(f"{path.name} is not a PNG file")
    if blob[12:16] != b"IHDR":
        raise ValueError(f"{path.name} has no IHDR chunk")
    width = int.from_bytes(blob[16:20], "big")
    height = int.from_bytes(blob[20:24], "big")
    return width, height


def publish_entry():
    if digest_of(PAGE) != EXPECTED_DIGEST:
        raise ValueError("vendored entry.png failed its digest check")
    width, height = dimensions_of(PAGE)
    if width > EDGE_LIMIT or height > EDGE_LIMIT:
        raise ValueError("entry.png is larger than 1024x1024")
    if PAGE.stat().st_size > SIZE_LIMIT:
        raise ValueError("entry.png is larger than 1 MiB")
    out_dir = Path(environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    target.write_bytes(PAGE.read_bytes())
    if digest_of(target) != EXPECTED_DIGEST:
        raise ValueError("the copied entry.png does not match the vendored page")
    copied_width, copied_height = dimensions_of(target)
    if (copied_width, copied_height) != (width, height):
        raise ValueError("the copied entry.png has different dimensions")
    size = target.stat().st_size
    print(f"entry.png -> {target} ({size} bytes, {width}x{height})")


if __name__ == "__main__":
    publish_entry()
