#!/usr/bin/env python3
"""Check that every C header has an include guard named after its file.

  check_guards.py [FOLDER ...]     default folder: src

For src/ring_buf.h the expected guard is RING_BUF_H: the file name in upper
case with every character that is not a letter or digit replaced by '_'.
Prints one line per problem. Exit code 0 = all good, 1 = problems found.
"""
import re
import sys
from pathlib import Path


def expected_guard(path: Path) -> str:
    return re.sub(r"[^A-Z0-9]", "_", path.name.upper())


def check(path: Path):
    text = path.read_text(encoding="utf-8", errors="replace")
    guard = expected_guard(path)
    ifndef = re.search(r"^\s*#\s*ifndef\s+(\w+)", text, re.MULTILINE)
    if not ifndef:
        return f"{path}: no include guard (expected {guard})"
    if ifndef.group(1) != guard:
        return f"{path}: guard is {ifndef.group(1)}, expected {guard}"
    if not re.search(r"^\s*#\s*define\s+" + re.escape(guard) + r"\b", text, re.MULTILINE):
        return f"{path}: #ifndef {guard} has no matching #define"
    return None


def main():
    if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        return 0
    folders = [Path(a) for a in sys.argv[1:]] or [Path("src")]
    headers = sorted(h for f in folders for h in f.rglob("*.h"))
    problems = [p for p in (check(h) for h in headers) if p]
    for problem in problems:
        print(problem)
    print(f"{len(headers)} header(s) checked, {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
