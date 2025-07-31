import os

def clear_saved_passwords():
    FILENAME = "saved_passwords.txt"
    confirm = input("Are you sure you want to delete all saved passwords? (Y/N): ").strip().lower()

    # return the code if neither Y or N was entered.
    if not(confirm == "y" or confirm == "n"):
        print("Please enter Y or N only.")
        return clear_saved_passwords()

    if confirm == "y":
        if os.path.exists(FILENAME):
            os.remove(FILENAME)
            print("✅ All saved passwords have been deleted.")
        else:
            print("No saved passwords to delete.")

    else:
        print("Operation cancelled.")
