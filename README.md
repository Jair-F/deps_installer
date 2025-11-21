# 🛠️ deps_installer

![PyPI - Version](https://img.shields.io/badge/pypi-unpublished-lightgrey) ![Python](https://img.shields.io/badge/python-3.8%2B-blue)

Simple helper to bundle small installer scripts with a Python app and run
them at runtime (Windows only). The package looks for an `installers`
directory (default: `data/installers`) in the packaged resources and executes
each file found there. This lets you ship one executable or folder and have
# deps_installer

![Python](https://img.shields.io/badge/python-3.8%2B-blue)

Lightweight helper to bundle and run small installer scripts included with a
Python application. It locates a folder of installer files (default:
`data/installers`) in your package/executable and executes each file found.

Table of Contents
- Quick Start
- Usage
- Packaging (PyInstaller)
- Troubleshooting & Notes
- Security
- Contributing

## Quick Start

Programmatic call (fast):

```python
from deps_installer import install_deps
install_deps()  # uses 'data/installers' by default
```

Example CLI (provided sample):

```powershell
python src/example_use.py --install_deps
```

## Usage

- Function: `install_deps(installer_folder='data/installers')`
- Platform: Windows only — on other OSes the function prints a message and
  returns without running installers.

Notes:
- The function executes every file found in the provided folder using
  `subprocess.Popen`. Ensure files are executable and trusted.
- If you bundle with PyInstaller, use `--add-binary data:data` (see Packaging).

## Packaging (PyInstaller)

Embed the `data` folder so installer files are available at runtime. Example:

```powershell
pyinstaller -F --clean --distpath dist \
  --add-binary data:data \
  --runtime-tmpdir tmp \
  --name installer_try src/example_use.py
```

This places your `data` contents inside the executable runtime so
`install_deps()` can find `data/installers`.

## Troubleshooting & Notes

- Missing folder: `os.listdir` will raise if the folder does not exist. Create
  `data/installers` (or pass a different folder) before packaging.
- Interactive installers: test installers manually—automated installs should
  avoid blocking prompts.
- Admin rights: if installers require elevation, re-launch your app as admin
  (see `pyuac` usage in `src/example_use.py`).

## Security

This project executes files shipped with the package. Only include files
from trusted sources. For production use consider:
- restricting executable extensions (e.g. `.exe`, `.msi`, `.bat`)
- validating file hashes or signatures before execution
