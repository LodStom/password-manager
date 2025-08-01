import string
import random
import pyperclip
import saveNoneExistingPasswords

def password_maker(length, label):

    # Length must be greater than 6.
    if length < 6:
        return None, "❌ The length must be at least 6 characters."


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

    # Save password
    save_result = saveNoneExistingPasswords.save_password_unique(final_password, label)

    return final_password, save_result
