# Tasks for Claude in VS Code

These tasks finish the Zensical rework of *Python meets micro:bit*. They couldn't be done from Cowork, which could only create and overwrite files in this folder. It couldn't delete files, run git, access GitHub, download from GitHub, or write inside `.github/`.

Work on the `zensical` branch. Do the tasks in order and check with Damien before each one marked **Confirm first**.

## Context

- **Site generator:** Zensical 0.0.65 (pinned in `requirements.txt`). Config is `zensical.toml`. Pages are in `docs/`.
- **Preview:** `zensical serve`. **Build:** `zensical build --clean` (must report "No issues found").
- **Examples:** `docs/examples/<group>/<page>/<example>/main.py`, included in pages with `--8<-- "examples/..."` (pymdownx.snippets, base path `docs`).
- **Solutions:** `docs/solutions/<group>/<page>/<exercise>.py`.
- **Drivers:** one copy of each PiicoDev driver in `docs/drivers/`. `scripts/make_zip.py` builds `docs/downloads/microbit_tutorials.zip` and copies the drivers each page needs into every example folder (see `PAGE_DRIVERS`).
- **Colour scheme:** navy `#476088`, yellow `#ffc562`, coral `#ff6d74`, teal `#4fddc3`, blue `#61a8e8`, set in `docs/stylesheets/extra.css`. The bright colours are for callouts and dark-mode text only, because they are too light to read as text on white.
- **Checks:** `python scripts/check_explanations.py` confirms every "Code explanation" line number matches its example.
- **Page template:** video → one-sentence description → "Possible uses:" bullet list → Connect it → Set it up → Methods table → for each method: a short explanation, one example, then a collapsible `??? note "Code explanation"` box (`- line n → …`) → Documentation → Exercises.
- **Example rules:** each example uses its method once, with only the supporting code needed to see it work, and keeps the `# Setup` / `# Main loop` structure. Comments are structural only.
- **Writing style:** Australian English, written for Year 7/8 students, in Damien's voice from the original site:
    - an inclusive "we" voice in instructions and explanations ("we need to", "our program", "Let's")
    - PRIMM prompts in a `!!! primm "PRIMM"` (coral, styled in `docs/stylesheets/extra.css`) callout after every example: "1. **Predict** what you think will happen. Be specific. 2. **Run** the program. 3. Time to **investigate** the code. What does each line do?"
    - code explanations as `- **line n** → full sentence ending in a full stop.`
    - exercises start with a `!!! primm "PRIMM"` (coral, styled in `docs/stylesheets/extra.css`) callout containing "Time to **modify** the code and see what happens." and are phrased as questions ("Can you …?"), with "For example:" before any GIF
- **Rework plan:** the full audit and plan are in Damien's Claude project as `microbit_python_rework_plan.md`.

## 1. Add the two missing PiicoDev drivers

1. Download these into `docs/drivers/`:
    - `PiicoDev_RV3028.py` from <https://github.com/CoreElectronics/CE-PiicoDev-RV3028-MicroPython-Module>
    - `PiicoDev_RGB.py` from <https://github.com/CoreElectronics/CE-PiicoDev-RGB-LED-MicroPython-Module>

    Use the micro:bit-friendly minified version from the repo's `min/` folder if there is one, matching the other drivers in `docs/drivers/`.
2. Run `python scripts/make_zip.py`. Expected: no `WARNING` lines.

## 2. Check the RTC and RGB LED pages against the driver source

Read the two new drivers and confirm or fix these assumptions in `docs/piicodev-inputs/rtc.md`, `docs/piicodev-outputs/rgb-led.md` and their examples:

- `wheel` is a module-level function imported with `from PiicoDev_RGB import PiicoDev_RGB, wheel`, and `h` ranges from `0` to `1`.
- `setBrightness()` needs `show()` afterwards to take effect.
- `rtc.timestamp()` reads the clock each time it is called, rather than returning stored values.
- `getDateTime()` fills in `rtc.weekday` with the day's name (the `getDateTime()` section says so).
- `rtc.ampm = "24"` is valid, and `year` accepts `2026`.

If anything differs, update the example, its code explanation, the methods table and any affected solution. Then run `python scripts/check_explanations.py` and `zensical build --clean`.

## 3. Delete leftover files in `docs/` — Confirm first

These are no longer used by any page:

- `docs/examples/piicodev/oled/show/`
- `docs/examples/other/glowbit/random/`
- `docs/examples/piicodev/rtc/weekday/`
- `docs/assets/debugger.png`
- `docs/assets/display_custom.gif`
- `docs/assets/display_image.gif`
- `docs/assets/display_show.gif`
- `docs/assets/first_program_folder.png`
- `docs/assets/first_program_name_folder.png`
- `docs/assets/first_program_open_folder.png`

Before deleting, search the repo to confirm none of them are referenced. Then rebuild the zip and the site.

## 4. Remove the old Sphinx site — Confirm first

The old site is still on `main` and will be tagged before merging (task 8), so nothing is lost. Show Damien this list before deleting:

- `00_introduction.md` to `99_licencing.md` (all numbered pages in the root)
- `index.md` (root only; the new home page is `docs/index.md`)
- `conf.py`, `Makefile`, `make.bat`
- `_static/`, `assets/`, `python_files/`, `student_resources/`
- `%GIT%microbit_python/` (a stray chat history database)
- `notes.md`, `todo.md`, `license.txt` (duplicate of `LICENSE`)
- `microbit_python_logo.ico`, `microbit_python_logo.jpg` in the root (copies are in `docs/assets/`)
- `_build/` if present

Keep `LICENSE`, `README.md`, `.gitignore`, `.gitattributes`, `requirements.txt`, `zensical.toml`, `docs/`, `scripts/` and `.github/`.

Check `student_resources/` with Damien first. It holds `atmospheric_sensor.zip`, which the new site doesn't use.

## 5. Replace the deploy workflow

Overwrite `.github/workflows/write_to_gh_pages.yml` with the workflow below. It builds with Zensical and deploys with GitHub Pages Actions. It only runs on `main`, so pushing to `zensical` won't change the live site.

```yaml
name: Deploy site

# Runs only when changes are pushed to main
on:
  push:
    branches: [ main ]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - uses: actions/configure-pages@v6
      - uses: actions/checkout@v7
      - uses: actions/setup-python@v6
        with:
          python-version: 3.x
      - run: pip install -r requirements.txt
      - run: zensical build --clean
      - uses: actions/upload-pages-artifact@v5
        with:
          path: site
      - uses: actions/deploy-pages@v5
        id: deployment
```

The action versions come from Zensical's own template. Confirm each version exists on GitHub before committing.

## 6. Update `README.md`

Replace the Sphinx-era README with:

- what the site is and who it is for (Year 7/8 students, BBC micro:bit v2, PiicoDev, Thonny)
- how to preview it (`pip install -r requirements.txt`, then `zensical serve`)
- how to rebuild the student zip (`python scripts/make_zip.py`)
- how to check explanations (`python scripts/check_explanations.py`)
- the folder layout from the Context section above
- the licences: GPLv3 for code, CC BY-NC-SA 4.0 for content

## 7. Final checks

1. Run `python scripts/make_zip.py`. Expected: no warnings.
2. Run `python scripts/check_explanations.py`. Expected: `0 issue(s) found`.
3. Run `zensical build --clean`. Expected: `No issues found`.
4. Check every external link in `docs/` returns a working page. Report broken ones to Damien rather than guessing replacements.
5. Spell-check the pages for Australian English.
6. Commit to `zensical` and push.

## 8. Go live — Confirm first

1. Tag the current `main` as `v1-sphinx` and push the tag, so the old site can be restored.
2. Merge `zensical` into `main` and push.
3. Change the Pages source to GitHub Actions: in the repo settings go to **Settings** → **Pages** → **Source**, or run `gh api -X PUT repos/damom73/microbit_python/pages -f build_type=workflow`.
4. Watch the **Deploy site** workflow run, then check that <https://damom73.github.io/microbit_python/> shows the new site.
5. Once the new site is confirmed working, the old `gh-pages` branch can be deleted. **Confirm first.**

## Tasks for Damien (not for Claude)

- Run every example and exercise solution on a micro:bit v2 with the PiicoDev modules, especially:
    - the RGB LED `wheel()` example
    - the RTC examples
    - the OLED `rotate()` example
    - the servo calibration values
    - the magnet threshold in the Compass Exercise 4 solution
- Check the Display Exercise 9 solution matches the glasses picture.
- Decide on the Sound Exercise 2 (College Song) solution.
