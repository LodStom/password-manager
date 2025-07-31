import os
from datetime import datetime

def save_password_unique(password, filename="saved_passwords.txt"):
    label = input("What is this password for? (e.g., Gmail, Facebook): ").strip()
    # Read existing passwords into a set for fast lookup
    existing_passwords = set()
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                stripped_line = line.strip()
                if not stripped_line:
                    continue
                parts = stripped_line.split()
                if len(parts) == 0:
                    continue
                existing_passwords.add(parts[0])

    if password in existing_passwords:
        print("⚠️ Password already saved. Not saving duplicate.")
    else:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(filename, "a") as file:
            file.write(f"{password}  ({timestamp}) for {label}\n")
        print(f"✅ Password saved to {filename}")

