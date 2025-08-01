import os

FILENAME = "saved_passwords.txt"


def view_saved_password():
    if not os.path.exists(FILENAME):
        return ""

    with open(FILENAME, "r") as file:
        return file.read().strip()
