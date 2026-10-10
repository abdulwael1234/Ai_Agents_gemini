---
name: commit-style
description: The commit message convention of this repository. Use when writing a commit message, committing changes, or reviewing whether a commit message is acceptable.
---

Format: `<type>(<module>): <summary> [<ticket>]`

- type is one of: feat, fix, test, refactor, docs, build.
- module is the file or component touched, for example ringbuf.
- summary is imperative, lower case, at most 60 characters, no full stop.
- ticket is the ID the user gave. If none was given, ask for it; never invent one.
- One logical change per commit. If the diff mixes two, propose two commits.

Show the message and wait for approval before committing.
