#+ deps_installer

Simple helper to bundle small installer scripts with a Python app and run
them at runtime (Windows only). The package looks for an `installers`
directory (default: `data/installers`) in the packaged resources and executes
each file found there. This lets you ship one executable or folder and have
supporting installers run automatically or on-demand.

**Key points**
- **Default installer folder:** `data/installers`
- **Main function:** `install_deps(installer_folder='data/installers')`
- **Platform:** Windows only (function is a no-op on other OSes)

**Why use this**
- Ship one EXE or directory to end users and include auxiliary installer
	executables, batch files, or scripts in `data/installers`.
- Run installers programmatically or via a command-line flag in your app.

**Note:** The module executes files found in the installer folder. Only use
trusted installer files—executing arbitrary files is a security risk.

**Example package layout**

```
project_root/
├─ data/
│  └─ installers/
│     ├─ setup_driver.exe
│     └─ install_helper.bat
├─ src/
│  ├─ example_use.py
│  └─ deps_installer/
│     ├─ __init__.py
│     └─ deps_installer.py
├─ pyproject.toml
└─ README.md
```

**How it works (brief)**
- Call `install_deps()` and the module will look up the resource path and
	iterate the files in the installer folder. Each file is executed using
	`subprocess.Popen`.

**Important behavior**
- The function only runs on Windows and will print `not on windows - not installing`
	on other platforms.
- Files in `data/installers` must be executable (e.g. `.exe`, `.msi`, `.bat`).

**Usage — programmatic**

Import and call the function in Python:

```python
from deps_installer import install_deps

# Uses the default folder 'data/installers'
install_deps()

# Or point to a different folder included in your package/data
install_deps(installer_folder='data/my_installers')
```

**Usage — example CLI**

The repository includes `src/example_use.py` to demonstrate a simple flag-based
approach. Example:

```powershell
# From project root
python src/example_use.py --install_deps
```

`example_use.py` shows how to optionally re-launch with elevation (example uses
`pyuac`) and then call `deps_installer.install_deps()` when `--install_deps` is
given.

**Packaging with PyInstaller**

When bundling into a single-file EXE, include the `data` folder so the
installer files are available at runtime. Example PyInstaller command (run
from project root):

```powershell
pyinstaller -F --clean --distpath dist \
	--add-binary data:data \
	--runtime-tmpdir tmp \
	--name installer_try src/example_use.py
```

- `--add-binary data:data` embeds the local `data` folder into the exe under
	the `data` path (so the code can access `data/installers`).
- `--runtime-tmpdir tmp` makes PyInstaller extract files into a `tmp` runtime
	directory instead of the OS temp folder.

**Build distribution (wheel / sdist)**

If you want a distributable Python package, use `build`:

```powershell
pip install build
python -m build
```

That will create `.whl` and `.tar.gz` files in `dist/`.

**Troubleshooting & tips**
- If the installer folder is missing `os.listdir` will raise an exception—ensure
	`data/installers` exists before packaging.
- Test each installer manually before bundling to ensure it runs without
	interactive prompts (or handle prompts in your packaging flow).
- If installers require admin rights, re-launch your app with elevation
	(see `pyuac` usage in `src/example_use.py`).

**Security note**
This project executes files present in the bundled data folder. Only include
trusted installers and consider adding integrity checks (signatures or hashes)
before executing files in production.

**Project status & suggested improvements**
- Add error handling for a missing or empty installer folder.
- Add filtering so only allowed file extensions are executed (e.g. `.exe`,
	`.msi`, `.bat`).
- Add a `--dry-run` mode that lists installers without executing them.
- Add unit tests and CI; include a `LICENSE` file and `CONTRIBUTING.md`.

**Contributing**
- Open an issue or submit a pull request. Add tests for new features and keep
	changes small and focused.

**License & Contact**
- Add a `LICENSE` file to the repository to make the license explicit.
- For questions, open an issue in the repository.