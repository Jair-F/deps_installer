
# Usage
the concept is to make a folder data/installers that is added to the pyinstaller if used and a single function is executed - install_deps that scans the files in the directory and executes each file.
then all the dependencies are installed and the user dont has to download each by hand himself.
like this you also just give them one exe file or one directory and the rest will be extracted and installed by the script.
the module makes this easier.
the installation can be executed on the first time running the file or like in the example by using a flag in the command line to trigger it.

## build exe
`pyinstaller -F --clean --distpath dist --add-binary data:data --runtime-tmpdir tmp --name installer_try main.py`

## build pypi
`python -m build`