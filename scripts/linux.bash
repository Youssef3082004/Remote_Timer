#!/usr/bin/env bash

set -e

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
PYTHON_EXE="$PROJECT_DIR/.venv/bin/python"

if [ ! -x "$PYTHON_EXE" ]; then
    echo "Virtual environment not found. Creating .venv..."
    python3 -m venv "$PROJECT_DIR/.venv"
    "$PYTHON_EXE" -m pip install -r "$PROJECT_DIR/requirements.txt"
fi

TEMP_LAUNCHER="$(mktemp "${TMPDIR:-/tmp}/timer.XXXXXX")"
trap 'rm -f "$TEMP_LAUNCHER"' EXIT

printf '#!/usr/bin/env bash\ncd %q\nexec %q main.py "$@"\n' \
    "$PROJECT_DIR" "$PYTHON_EXE" > "$TEMP_LAUNCHER"

sudo install -m 755 "$TEMP_LAUNCHER" /usr/local/bin/timer

echo "Installed successfully. Run 'timer' from any terminal."
