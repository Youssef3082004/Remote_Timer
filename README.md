<div align="center">

# ⏱️ Timer

**A simple command-line time tracker and computer activity helper**

Record focused time, deduct breaks, keep your computer active, and review your
daily totals—all from the terminal.

</div>


## ✨ Features

| Feature | Description |
| --- | --- |
| 🖱️ Keep active | Moves the mouse periodically to keep the computer active. |
| ⏳ Record time | Adds elapsed time to today's local record. |
| ➖ Deduct time | Subtracts elapsed time from the newest records first. |
| 📅 Daily history | Shows all records or filters them by date. |
| 📊 Total time | Displays the combined recorded time as `HH:MM:SS`. |
| 🎨 Colored output | Uses clear colors for prompts, status updates, and errors. |
| 💾 Local storage | Keeps your data locally in a readable JSON file. |

## 🚀 Quick start

### 1. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

> On Windows, activate it with `.venv\Scripts\activate`.

### 2. Install the dependencies

```bash
python3 -m pip install -r requirements.txt
```

### 3. Start the application

```bash
python3 main.py
```

> Run this command from the project root so the application reads and writes
> the correct `time.json` file.

### 4. Optional: install the `timer` terminal command

You can install the application as a `timer` command and run it from any
terminal. From the project root, use the setup script for your operating
system.

#### Linux

```bash
bash scripts/linux.bash
```

The Linux installer uses `sudo` to install the command in `/usr/local/bin`.
If `.venv` does not exist, the installer creates it and installs the required
Python packages automatically.

#### macOS

```bash
bash scripts/mac.bash
```

The macOS installer uses `sudo` to install the command in `/usr/local/bin`.
If `.venv` does not exist, the installer creates it and installs the required
Python packages automatically.

#### Windows

In Command Prompt:

```bat
scripts/windows.bat
```

Or in PowerShell:

```powershell
.\scripts\windows.bat
```

The Windows installer adds the command to your user `PATH`. Open a new
terminal after it finishes.

After installing on any platform, start the application with:

```bash
timer
```

## 🎮 Menu options

When the application starts, enter a number from `1` to `6`:

| Option | Action |
| :---: | --- |
| `1` | Keep the computer active and add the elapsed time to today's record. |
| `2` | Start a timer and subtract the elapsed time from the newest records. |
| `3` | Keep the computer active without recording time. |
| `4` | Display the recorded time for every day. |
| `5` | Display the record for a date entered as `DD/MM/YYYY`. |
| `6` | Display the total time recorded across all days. |

Press <kbd>Ctrl</kbd> + <kbd>C</kbd> to stop an active timer or mouse-moving
session. Option `1` saves the elapsed time before stopping.

## 📦 Requirements

- Python 3.10 or newer
- Pydantic 2.x
- PyAutoGUI 0.9.54 or newer
- Colorama 0.4.6
- A graphical desktop session for options `1` and `3`

PyAutoGUI may require additional system packages on Linux. If installation
fails, consult the
[PyAutoGUI installation guide](https://pyautogui.readthedocs.io/en/latest/install.html)
for your distribution.

## 🗃️ Data storage

Records are stored locally in `time.json`. Each item contains a date and the
recorded duration in seconds:

```json
[
  {
    "date": "18/10/2026",
    "seconds": 3600
  }
]
```

The application formats durations as `HH:MM:SS` when displaying them. The
deduction timer removes time from the most recent records first.

## 🧱 Project structure

```text
timer/
├── Controller/
│   ├── Cursor.py        # Mouse movement and optional time recording
│   └── Timer.py         # Elapsed-time tracking
├── Model/
│   └── Day.py           # Daily time-record model
├── data/
│   └── jsondata.py      # JSON persistence and record queries
├── helper/
│   ├── Colors.py        # Shared terminal color palette
│   └── Formating.py     # Duration formatting
├── main.py              # Command-line menu
├── requirements.txt     # Python dependencies
├── scripts/
│   ├── linux.bash       # Linux command installer
│   ├── mac.bash         # macOS command installer
│   └── windows.bat      # Windows command installer
└── time.json            # Saved time records
```

## 🛠️ Troubleshooting

**`ModuleNotFoundError` appears**

Activate the virtual environment and reinstall the dependencies:

```bash
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

**Mouse movement does not work**

Make sure you are running the application in a graphical desktop session and
that your operating system allows terminal applications to control the mouse.

---

<div align="center">
Made for simple, local time tracking.
</div>
