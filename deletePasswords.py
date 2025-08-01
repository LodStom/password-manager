import os

FILENAME = "saved_passwords.txt"

def clear_saved_passwords():

    # Delete all saved passwords without needing console input.
    if os.path.exists(FILENAME):
        os.remove(FILENAME)
        return "✅ All saved passwords have been deleted."
    else:
        return "No saved passwords to delete."

