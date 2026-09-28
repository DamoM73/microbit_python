"""Build the student tutorial zip from docs/examples.

Run from the repository root:  python scripts/make_zip.py
Creates docs/downloads/microbit_tutorials.zip containing:
    microbit_tutorials/<page>/<example>/main.py (+ any driver files in that folder)
"""
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parent.parent
EXAMPLES = ROOT / "docs" / "examples"
OUT = ROOT / "docs" / "downloads" / "microbit_tutorials.zip"


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zf:
        for file in sorted(EXAMPLES.rglob("*")):
            if file.is_file():
                # Drop the group level (microbit/, piicodev/ ...) so students see page folders
                parts = file.relative_to(EXAMPLES).parts[1:]
                zf.write(file, Path("microbit_tutorials", *parts))
    print(f"Wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
