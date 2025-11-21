import argparse
import sys

import pyuac
import deps_installer

RUN_AS_ADMIN = False

if __name__ == "__main__":
    if RUN_AS_ADMIN and not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        pyuac.runAsAdmin()
        sys.exit(0)

    parser = argparse.ArgumentParser(description="A sample program using argparse.")
    parser.add_argument("--install_deps", action="store_true", help="Enable verbose output.")
    args = parser.parse_args()

    if args.install_deps:
        deps_installer.install_deps()
    else:
        print("running normally")
    