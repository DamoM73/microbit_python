"""Build the student tutorial zip from docs/examples.

Run from the repository root:  python scripts/make_zip.py
Creates docs/downloads/microbit_tutorials.zip containing:
    microbit_tutorials/<page>/<example>/main.py
plus the PiicoDev driver files each page needs (copied from docs/drivers).
"""
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parent.parent
EXAMPLES = ROOT / "docs" / "examples"
DRIVERS = ROOT / "docs" / "drivers"
OUT = ROOT / "docs" / "downloads" / "microbit_tutorials.zip"

UNIFIED = "PiicoDev_Unified.py"
# Driver files needed by every example folder of each page
PAGE_DRIVERS = {
    "atmospheric": [UNIFIED, "PiicoDev_BME280.py"],
    "colour": [UNIFIED, "PiicoDev_VEML6040.py"],
    "distance": [UNIFIED, "PiicoDev_VL53L1X.py"],
    "potentiometer": [UNIFIED, "PiicoDev_Potentiometer.py"],
    "button": [UNIFIED, "PiicoDev_Switch.py"],
    "rtc": [UNIFIED, "PiicoDev_RV3028.py"],
    "rgb_led": [UNIFIED, "PiicoDev_RGB.py"],
    "oled": [UNIFIED, "PiicoDev_SSD1306.py", "font-pet-me-128.dat", "piicodev-logo.pbm"],
    "servo": [UNIFIED, "PiicoDev_Servo.py"],
}


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    missing = set()
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zf:
        for main_py in sorted(EXAMPLES.rglob("main.py")):
            # Keep only <page>/<example>, dropping any group level (microbit/, piicodev/ ...)
            page, example = main_py.parent.relative_to(EXAMPLES).parts[-2:]
            folder = Path("microbit_tutorials", page, example)
            zf.write(main_py, folder / "main.py")
            for name in PAGE_DRIVERS.get(page, []):
                driver = DRIVERS / name
                if driver.exists():
                    zf.write(driver, folder / name)
                else:
                    missing.add(name)
    print(f"Wrote {OUT.relative_to(ROOT)}")
    for name in sorted(missing):
        print(f"WARNING: docs/drivers/{name} is missing, so it was left out of the zip")


if __name__ == "__main__":
    main()
