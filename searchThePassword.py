import os

def search_password():
    if not os.path.exists("saved_passwords.txt"):
        print("❌ No saved passwords found.")
        return

    label = input("Enter a keyword to search for: ").strip()
    found = False

    with open("saved_passwords.txt", "r") as file:
        for line in file:
            if label.lower() in line.lower():  # Case-insensitive match
                print(line.strip())
                found = True

    if not found:
        print("❌ No matching passwords found.")
