#!/usr/bin/env python3
from guizero import App, TextBox, Text, PushButton, ButtonGroup
import os


def create_shortcut():
    """Create the shortcut."""
    filename = filename_input.value
    name = name_input
    exec_path = exec_path_input
    icon_path = icon_path_input
    term = term_input
    if term.value == "no":
        term = "false"
    else:
        term = "true"
    shortcut = f"""
[Desktop Entry]
Name={name.value}
Exec={exec_path}
Icon={icon_path}
Terminal={term}
Type=Application
Categories=Application
Hidden=false
                """
    with open(f"{filename}.desktop", mode="w", encoding="utf-8") as file:
        file.write(shortcut)
        file.close()
    os.system(f"mv {filename}.desktop ~/.local/share/applications/")
    os.system(f"chmod +x ~/.local/share/applications/{filename}.desktop")
    Text(app, text="Done, moved to ~/.local/share/applications")


def select_exec_path():
    """Allow you to select to exec path."""
    global exec_path_input
    exec_path_input = app.select_file()


def select_icon_path():
    """Allow you to select the icon path"""
    global icon_path_input
    icon_path_input = app.select_file()


def confirmation():
    """Confirm if you want to create the shortcut."""
    confirm = app.yesno("Are you Sure?", "Do you want to continue?")
    if confirm is True:
        create_shortcut()


def application():
    """Is the actual program."""
    global app, filename_input, name_input, exec_path_input, icon_path_input, term_input
    app = App(title="Shortcut Creator")
    Text(app, text="Enter the filename you want.")
    filename_input = TextBox(app, width=15)
    Text(app, text="Enter the name you want for your shortcut.")
    name_input = TextBox(app, width=15)
    Text(app, text="Select the exceutable path.")
    exec_path_input = PushButton(app, command=select_exec_path, text="Select Here")
    Text(app, text="Select the icon path")
    icon_path_input = PushButton(app, command=select_icon_path, text="Select Here")
    Text(app, text="Do you want to run in terminal mode?")
    term_input = ButtonGroup(app, options=["no", "yes"], selected="no")
    PushButton(app, command=confirmation, text="Click when done")
    app.display()


def main():
    """Run the actual program."""
    application()


if __name__ == '__main__':
    uname = os.uname()
    if uname.sysname == "Linux":
        main()
    else:
        app = App()
        app.warn(title="Warning", text="MacOS not supported by this script.")
        exit()
