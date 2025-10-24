# Orga-Nice

**What it is**
A tiny GUI tool (Tkinter) that tidies a selected folder by moving files into categorized subfolders. Choose a single extension (e.g. `pdf`) or organize all known types at once. Includes preview, undo, dark mode, and optional audio (pygame).

**Key features**

* Organize specific format or all files
* Preview before moving
* Undo last organize (restores files, removes empty folders)
* Dark mode + optional background music & SFX

**Requirements**

* Python 3.8+
* `pygame` (audio)
* `tkinter` (usually bundled; on Linux install system package `python3-tk`)

**Install (quick)**

```bash
python -m venv .venv
# activate venv
pip install pygame
```

**Run**

```bash
python orga_nice.py
```

Select a folder → preview → confirm.
