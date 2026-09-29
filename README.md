# Python meets micro:bit

*Python meets micro:bit* is a set of tutorials for learning Python with the BBC micro:bit v2. It is written for Year 7/8 students, uses the Thonny editor, and covers the micro:bit's built-in features as well as PiicoDev sensor and output modules.

The site is live at <https://damom73.github.io/microbit_python/>.

## Preview the site

The site is built with [Zensical](https://zensical.org/).

```bash
pip install -r requirements.txt
zensical serve
```

To check the full build, run `zensical build --clean`. It should report `No issues found`.

## Rebuild the student zip

```bash
python scripts/make_zip.py
```

This builds `docs/downloads/microbit_tutorials.zip` and copies the PiicoDev drivers each page needs into every example folder (see `PAGE_DRIVERS` in the script). It should print no `WARNING` lines.

## Check code explanations

```bash
python scripts/check_explanations.py
```

This confirms every "Code explanation" line number matches its example. It should report `0 issue(s) found`.

## Folder layout

| Path | Contents |
| --- | --- |
| `zensical.toml` | Site configuration |
| `docs/` | Site pages |
| `docs/examples/<group>/<page>/<example>/main.py` | Examples, included in pages with `--8<-- "examples/..."` |
| `docs/examples/<group>/<page>/exN_*/main.py` | Exercise starter files |
| `docs/solutions/<group>/<page>/<exercise>.py` | Exercise solutions |
| `docs/drivers/` | One copy of each PiicoDev driver |
| `docs/downloads/` | The student zip |
| `docs/stylesheets/extra.css` | Colour scheme and custom callouts |
| `scripts/` | Zip builder and explanation checker |

## Licence

- Code is licensed under the [GNU General Public License v3.0](LICENSE).
- Content is licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/).
