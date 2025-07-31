import generator
import viewPasswords
import deletePasswords
import searchThePassword

def main_menu():
    while True:
        print("\n--- Password Generator Menu ---")
        print("1. Generate a password")
        print("2. View saved passwords")
        print("3. Clear saved passwords")
        print("4. Search the password")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
           generator.password_maker()
        elif choice == "2":
            viewPasswords.view_saved_password()
        elif choice == "3":
            deletePasswords.clear_saved_passwords()
        elif choice == "4":
            searchThePassword.search_password()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 5.")

main_menu()
