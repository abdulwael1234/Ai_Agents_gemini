#!/bin/sh
# Usage: scripts/size.sh <variant>   prints "section bytes" for the built objects
size -A build/*.o | awk '$2 ~ /^[0-9]+$/ && $1 ~ /^\.(text|data|bss)$/ { s[$1] += $2 } END { for (k in s) print k, s[k] }'
