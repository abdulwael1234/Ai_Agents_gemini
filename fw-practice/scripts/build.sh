#!/bin/sh
# Usage: scripts/build.sh <variant>   (dev or release)
set -e
mkdir -p build
OPT="-O0"; [ "$1" = "release" ] && OPT="-Os"
for f in src/*.c; do
  gcc -std=c99 $OPT -Wall -Wextra -Werror -Isrc -c "$f" -o "build/$(basename "$f" .c).o"
done
echo "Build OK ($1)"
