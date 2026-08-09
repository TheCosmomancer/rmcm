#!/usr/bin/env bash
set -e

if ! command -v python3 &>/dev/null; then
        echo "Could not detect python. Please install python before proceeding." >&2
        exit 1
fi

chmod +x rmcm.py
sudo install -m 755 rmcm.py /usr/local/bin/rmcm

echo "Moved rmcm.py to /usr/local/bin/rmcm
You can now run it by typing: rmcm"