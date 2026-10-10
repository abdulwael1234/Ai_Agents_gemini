#!/bin/sh
# Usage: scripts/lint.sh <files...>   extra compiler warnings as a stand-in for a MISRA checker
gcc -std=c99 -fsyntax-only -Wall -Wextra -Wconversion -Wshadow -Isrc "$@"
