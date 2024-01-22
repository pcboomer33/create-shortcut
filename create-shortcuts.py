#!/usr/bin/env python3
import os
import time

def create_shortcut(name, exec_path, icon_path, file_name, term="false"):
    """Writes a shortcut file to ~/.local/share/applications."""
    shortcut = f"""
[Desktop Entry]
Name={name}
Exec={exec_path}
Icon={icon_path}
Terminal={term}
Type=Application
Categories=Application
Hidden=false
                """
    with open(f"{file_name}.desktop", mode="w", encoding="utf-8") as file:
        file.write(shortcut)
        file.close()


def main():
    """Does the magic stuff."""
    print("WARNING!!! THIS PROGRAM DOESN'T WORK ON MACOS NOR WINDOWS, ONLY LINUX")
    print("You have to put the absolute path.")
    time.sleep(2)
    filename_input = input("Please enter the filename you want (no need for .desktop) ")
    name = input("Enter the shortcut name ")
    exec_path = input("Enter the executable path. (make sure its executable) ")
    icon_path = input("Please enter icon path ")
    term = input("Run in terminal mode? \n (y for terminal mode, n for normal mode) ")
    term = term.lower()
    if term == "y":
        create_shortcut(name, exec_path, icon_path, filename_input, term="true")
    else:
        create_shortcut(name, exec_path, icon_path, filename_input)
    os.system(f"mv {filename_input}.desktop ~/.local/share/applications/")
    os.system(f"chmod +x ~/.local/share/applications/{filename_input}.desktop")
    print("done. moved to ~/.local/share/applications/")
    print("reboot your system")

if __name__ == '__main__':
    uname = os.uname()
    if uname.sysname == "Linux":
        main()
    else:
        print("MacOS not supported by this script.")
        exit()
