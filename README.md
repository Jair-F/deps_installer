
## build
`pyinstaller -F --clean --distpath dist --add-binary data:data --runtime-tmpdir tmp --name installer_try main.py`

- one file: -F
- one dir: -D
- -i icons/icon.ico



rest reqs
pyinstaller
pyuac
pywin32