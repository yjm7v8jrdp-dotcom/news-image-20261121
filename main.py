"""Entry for make.fun bounty news-image-20261121: Saturday 21 November 2026 world news."""

from pathlib import Path
import os
import shutil


def main() -> None:
    root = Path(__file__).resolve().parent
    src = root / "entry.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dst = out_dir / "entry.png"
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    main()
