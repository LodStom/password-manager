import os

FILENAME = "saved_passwords.txt"

def search_password(term):
    matches = []
    if not os.path.exists(FILENAME):
        return matches
    term = term.lower().strip()
    with open(FILENAME, "r") as file:
        for line in file:
            if term in line.lower():
                matches.append(line.strip())
    return matches
