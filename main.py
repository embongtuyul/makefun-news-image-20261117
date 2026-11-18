"""news-image-20261117 entry: copy the finished front-page image to the output dir.

The image (image.jpg, JPEG bytes) is written verbatim to
$MAKEFUN_OUTPUT_DIR/entry.png. The competition accepts JPEG content in entry.png
(the format is told apart by the file's first bytes), and the program is fully
deterministic: the same input bytes produce the same output bytes every run.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "image.jpg")


def main():
    with open(SOURCE, "rb") as f:
        data = f.read()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.png")
    with open(out_path, "wb") as f:
        f.write(data)
    # Verify the copy is complete: the written file must match the source bytes.
    if os.path.getsize(out_path) != len(data):
        raise RuntimeError("entry.png size mismatch: wrote %d bytes, expected %d"
                           % (os.path.getsize(out_path), len(data)))
    print("wrote %d bytes to %s" % (len(data), out_path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
