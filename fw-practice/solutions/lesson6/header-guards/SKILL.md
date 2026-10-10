---
name: header-guards
description: Checks that every C header has an include guard named after its file. Use after adding or renaming a header, when asked to check include guards, and before a commit that touches header files.
---

1. Run `python3 scripts/check_guards.py --help` in this skill's folder once to see the options.
2. Run it on the folders that hold headers, `src` by default.
3. For each problem line, fix the guard in that header: both the `#ifndef` and the `#define`.
4. Never touch headers under `gen/` or `vendor/`. Report them instead.
5. Run the script again and report the summary line.
