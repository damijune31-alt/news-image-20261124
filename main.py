"""news-image-20261124 entry: copy the front-page image to the output dir.

The image (entry.png, beside this file) is a 1024x1024 newspaper front page
summing up Tuesday 24 November 2026: Ukraine sinks the Russian corvette
Merkury off Libya, the US blacklists Megaspeed, Huang returns at Nvidia,
plus the Indonesia factory fire, Zelensky's call for talks, and COP31's
collapse. Standard library only, no network, deterministic output.
"""
import os
import shutil
import sys


MAX_BYTES = 1024 * 1024


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if os.path.getsize(src) > MAX_BYTES:
        sys.exit("entry.png exceeds 1 MiB")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print("wrote " + dst)


if __name__ == "__main__":
    main()
