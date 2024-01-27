#!/usr/bin/env python3

import os

def main():
    username = os.getlogin()
    shortcut = f"""
    [Desktop Entry]
    Name=Shortcut Creator
    Exec=/usr/bin/create-shortcut
    Icon=/home/{username}/.local/share/application/shortcut-icon.png
    Terminal=false
    Type=Application
    Categories=Application
    Hidden=false
                """
    os.system("pip3 install guizero")
    os.system("cp create-shortcut.py /usr/bin/create-shortcut")
    with open(f"create-shortcut.desktop", mode="w", encoding="utf-8") as file:
        file.write(shortcut)
        file.close()
    os.system(f"mv create-shortcut.desktop ~/.local/share/applications/")
    os.system(f"cp shortcut-icon.png ~/.local/share/applications/")
    os.system(f"chmod +x ~/.local/share/applications/create-shortcut.desktop")
    print("Done installing! application moved to /usr/bin")

if __name__ == '__main__':
    uname = os.uname()
    if uname.sysname == "Linux":
        main()
    else:
        print("Mac OS is not supported by this script")
