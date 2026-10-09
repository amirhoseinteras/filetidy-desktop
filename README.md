# FileTidy for Windows

Organize mixed download folders into categories with a safe preview and one-step undo.

**Version:** 1.0.0. Works fully offline, with no accounts or analytics.

## Download / دانلود

Use GitHub Releases: **FileTidy-Setup.exe** to install (Start Menu, desktop shortcut, uninstall) or **FileTidy-Portable.zip** to run without installing. Both builds are unsigned. Windows SmartScreen can warn about unsigned programs.

## Run from source

Requires Windows and Python 3.10+ with Tkinter. Run: python filetidy.py

## Important

No network or API; do not run twice before undo. Skips symbolic links.

## License / مشارکت

MIT for original source code. Bug reports, translations and genuine contributions are welcome. Do not submit fake stars, downloads, or meaningless pull requests.

## Reproducible Windows builds

Install Python 3.10+, run 'python -m pip install -r requirements.txt pyinstaller' then 'python build_windows.py'. Outputs are under dist/. The installer provides per-user installation and uninstall; it never requires administrator access.
