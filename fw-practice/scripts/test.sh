#!/bin/sh
# Usage: scripts/test.sh [module]   runs tests/test_<module>.c, or all tests
set -e
mkdir -p build
for t in tests/test_${1:-*}.c; do
  name=$(basename "$t" .c)
  gcc -std=c99 -Wall -Wextra -Isrc "$t" src/*.c -o "build/$name"
  "./build/$name"
done
echo "All tests passed"
