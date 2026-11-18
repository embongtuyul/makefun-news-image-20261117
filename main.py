"""Copy the front-page image to the make.fun output directory.

The entry image is the file image.jpg next to this script; it is copied
byte-for-byte to $MAKEFUN_OUTPUT_DIR/entry.png. Deterministic: the same
bytes come out on every run.
"""

import os
import pathlib


def main():
    here = pathlib.Path(__file__).resolve().parent
    source = here / "image.jpg"
    data = source.read_bytes()

    out_dir = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    target.write_bytes(data)
    # verify the copy landed intact: size must match the source exactly
    if target.stat().st_size != len(data):
        raise RuntimeError(
            f"short write: {target} is {target.stat().st_size} bytes, "
            f"expected {len(data)}"
        )
    print(f"wrote {len(data)} bytes to {target}")


if __name__ == "__main__":
    main()
