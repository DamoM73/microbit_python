"""Check every "Code explanation" box against the example it explains.

Run from the repository root:  python scripts/check_explanations.py

For each snippet include (--8<-- "path") followed by a ??? note "Code explanation" box:
- BAD      -> the explanation refers to a blank line, a comment, or a line past the end
- MISSING  -> a line of code has no explanation
"""
from pathlib import Path
import re
import sys

DOCS = Path(__file__).resolve().parent.parent / "docs"


def main():
    issues = 0
    for md in sorted(DOCS.rglob("*.md")):
        parts = re.split(r'--8<-- "([^"]+)"', md.read_text(encoding="utf-8"))
        for i in range(1, len(parts), 2):
            code = (DOCS / parts[i]).read_text(encoding="utf-8").split("\n")
            after = parts[i + 1].split("--8<--")[0]
            box = re.search(r'\?\?\? note "Code explanation"(.*?)(\n\S|\Z)', after, re.S)
            if not box:
                continue
            refs = []
            for start, end in re.findall(r"lines? (\d+)(?:–(\d+))?", box.group(1)):
                refs += range(int(start), int(end or start) + 1)
            for n in refs:
                if n > len(code) or not code[n - 1].strip() or code[n - 1].strip().startswith("#"):
                    print(f"BAD      {md.relative_to(DOCS)}  {parts[i]}  line {n}")
                    issues += 1
            for n, line in enumerate(code, 1):
                if line.strip() and not line.strip().startswith("#") and n not in refs:
                    print(f"MISSING  {md.relative_to(DOCS)}  {parts[i]}  line {n}: {line.strip()}")
                    issues += 1
    print(f"{issues} issue(s) found")
    sys.exit(1 if issues else 0)


if __name__ == "__main__":
    main()
