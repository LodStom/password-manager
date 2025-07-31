import os
def view_saved_password():
    FILENAME = "saved_passwords.txt"
    if not os.path.exists(FILENAME):
        print("No saved passwords found.")
        return
    print ("\n --- Saved Passwords ---")
    with open(FILENAME, "r") as file:
        content = file.read().strip()
        if content:
            print(content)
        else:
            print("No saved passwords found.")

    print("-----------------------\n")
