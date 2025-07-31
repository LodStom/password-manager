import string
import random
import pyperclip
import saveNoneExistingPasswords

def password_maker():
    # Ask the user the length of the password
    length = input("What is the desired length? (Minimum 6 characters): ")

    # Checks if the input is the int()
    if not length.isdigit():
        print("Please enter a Whole number(e.g. 6, 10, 250)")
        return password_maker()

    # Turns the length to int()
    length = int(length)

    # Checks if the length input is greater than 6
    if length < 6:
        print("❌ The length must be at least 6 characters.")
        return password_maker()


    # Character pools
    lower_char = string.ascii_lowercase
    upper_char = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Start with at least one of each required character type
    password = [
        random.choice(upper_char),
        random.choice(digits),
        random.choice(symbols)
    ]

    all_char = lower_char + symbols + upper_char + digits

    # Fill the rest of the password
    while len(password) < length:
        password.append(random.choice(all_char))

    # Shuffle and join to get the final password
    random.shuffle(password)
    final_password = ''.join(password)

    # Copy to clipboard
    pyperclip.copy(final_password)
    print(f"\n✅ Your password has been copied to the clipboard.")
    print(f"🔐 Generated password : {final_password}")

    # Save to txt
    saveNoneExistingPasswords.save_password_unique(final_password)
