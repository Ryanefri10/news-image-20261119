"""Ship the 19 November 2026 front page as this entry's image.

Next to this script sits entry.png: the front page for Thursday
19 November 2026, composed from that day's verified news. All this
program does is confirm the vendored page is exactly the one it
should be, then drop a byte-identical copy where the grader looks.
Python standard library only; no network, no third-party code, no
drawing at run time.
"""

import hashlib
import os
import struct

HERE = os.path.dirname(os.path.abspath(__file__))
PAGE_PATH = os.path.join(HERE, "entry.png")

# sha256 of the composed 19 November 2026 front page. The copy is
# checked against it, so a damaged or swapped vendored file fails
# loudly instead of entering the wrong picture.
PAGE_SHA256 = "5197959aab5ee48a228f9a722727edd45b710a67a616a618912bd2af381bf1f1"
MAX_BYTES = 1024 * 1024
MAX_EDGE = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def read_page():
    with open(PAGE_PATH, "rb") as handle:
        return handle.read()


def check_page(blob):
    """Raise unless blob is the expected whole 1024x1024 PNG."""
    if len(blob) > MAX_BYTES:
        raise ValueError("entry.png is larger than 1 MiB")
    if hashlib.sha256(blob).hexdigest() != PAGE_SHA256:
        raise ValueError("vendored entry.png failed its digest check")
    if blob[:8] != PNG_MAGIC:
        raise ValueError("entry.png is not a PNG file")
    if blob[12:16] != b"IHDR":
        raise ValueError("entry.png has no IHDR chunk")
    width, height = struct.unpack(">II", blob[16:24])
    if width > MAX_EDGE or height > MAX_EDGE:
        raise ValueError("entry.png is larger than 1024x1024")
    return width, height


def main():
    blob = read_page()
    width, height = check_page(blob)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    with open(target, "wb") as handle:
        handle.write(blob)
    with open(target, "rb") as handle:
        copied = handle.read()
    if copied != blob:
        raise ValueError("the copied entry.png does not match the vendored page")
    print("entry.png -> %s (%d bytes, %dx%d)" % (target, len(copied), width, height))


if __name__ == "__main__":
    main()
