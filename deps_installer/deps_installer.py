import os
import subprocess
import sys

def is_windows() -> bool:
    return sys.platform == 'win32'

def in_pyinstaller() -> bool:
    return getattr(sys, 'frozen', False)

def get_resource_path(relative_path) -> str:
    base_path = os.path.abspath(".")
    try:
        if in_pyinstaller():
            base_path = sys._MEIPASS
    except AttributeError:
        pass
    return os.path.join(base_path, relative_path)

def install_deps(installer_folder = 'data/installers') -> None:
    if not is_windows():
        print('not on windows - not installing')
        return

    print("Installing deps")

    installer_folder_path = get_resource_path(installer_folder)
    file_list = os.listdir(installer_folder_path)
    for install_file in file_list:
        installer_path = os.path.join(installer_folder_path, install_file)
        process = subprocess.Popen([installer_path], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process.wait()
    
    print("installed everything")
