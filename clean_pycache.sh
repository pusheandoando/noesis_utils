#!/usr/bin/env bash
# clean_pycache.sh





find . -type d -name "__pycache__" -print -exec rm -rf {} +
echo "[OK] All __pycache__ folders were deleted"