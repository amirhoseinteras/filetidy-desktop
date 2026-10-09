# FileTidy — Open-Source Windows Utility

Offline Windows file organizer for mixed folders with category preview and one-step undo.

[![Automated tests](https://github.com/amirhoseinteras/filetidy-desktop/actions/workflows/tests.yml/badge.svg)](https://github.com/amirhoseinteras/filetidy-desktop/actions/workflows/tests.yml)
[Download latest](https://github.com/amirhoseinteras/filetidy-desktop/releases/latest) · [Source code](https://github.com/amirhoseinteras/filetidy-desktop) · [Issues](https://github.com/amirhoseinteras/filetidy-desktop/issues)

**Version:** 1.0.0 · **Platform:** Windows · **License:** MIT

## Features
- Preview where files will be organized before applying any changes.
- Sort supported file types into categories such as Images and Audio.
- Undo the latest organizing pass to restore the original folder layout.
- Runs locally with no account, server, or analytics.

## Download for Windows

| Package | Download | Usage |
| --- | --- | --- |
| Installer | [FileTidy-Setup.exe](https://github.com/amirhoseinteras/filetidy-desktop/releases/latest/download/FileTidy-Setup.exe) | Install with Start Menu shortcut and uninstaller for the current user |
| Portable | [FileTidy-Portable.zip](https://github.com/amirhoseinteras/filetidy-desktop/releases/latest/download/FileTidy-Portable.zip) | Unzip and launch FileTidy.exe; no installation |
| Checksums | [SHA256SUMS.txt](https://github.com/amirhoseinteras/filetidy-desktop/releases/latest/download/SHA256SUMS.txt) | Verify the downloaded files |

**Important:** Release files are unsigned; Windows SmartScreen may display a warning. Check the source and published hashes before trusting an executable. Do not disable your security software to bypass warnings.

### Check download integrity

~~~powershell
Get-FileHash .\FileTidy-Setup.exe -Algorithm SHA256
~~~
Compare the output with the corresponding line of SHA256SUMS.txt from the same release.

## Requirements & limitations

Undo is intended for the latest organization operation; avoid running multiple passes before undo. Symbolic links are skipped. Always review the preview.

## Run from source

Windows and Python 3.10+ with Tkinter are required.

~~~powershell
python -m pip install -r requirements.txt
python filetidy.py
python -m unittest discover -s tests -v
~~~

The source tree includes build_windows.py and packaging/installer.py for reproducible Windows packaging.

## Support and development

- [Security](SECURITY.md) · [License](LICENSE) · [Changelog](CHANGELOG.md) · [Contributing](CONTRIBUTING.md)
- [Report bugs or request features](https://github.com/amirhoseinteras/filetidy-desktop/issues). Provide the OS version, steps, and expected/actual results.
- No telemetry or account is needed for these offline tools. The source code provides the authoritative feature specification.

## فارسی — راهنمای دانلود

**FileTidy** برنامه‌ای متن‌باز و رایگان برای ویندوز است. فایل Setup برای نصب و نسخه Portable ZIP برای اجرا بدون نصب ارائه شده است.
نسخه‌های اجرایی امضای دیجیتال ندارند. مقدار SHA-256 هر فایل را با فایل SHA256SUMS.txt داخل همان انتشار مقایسه کنید.

---
**Repository:** https://github.com/amirhoseinteras/filetidy-desktop · **Releases:** https://github.com/amirhoseinteras/filetidy-desktop/releases