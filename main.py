import tkinter as tk
from tkinter import messagebox, scrolledtext
import generator
import viewPasswords
import deletePasswords
import searchThePassword

# ------------------- GENERATE PASSWORD -------------------

def gui_generate_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number for password length.")
        return

    label = label_entry.get().strip()
    if not label:
        messagebox.showerror("Error", "Enter a label for this password.")
        return

    password, result_msg = generator.password_maker(length, label)

    if password is None:
        messagebox.showwarning("Warning", result_msg)
        return

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    messagebox.showinfo("Result", f"{result_msg}\nPassword copied to clipboard.")

# ------------------- VIEW PASSWORDS -------------------
def gui_view_passwords():
    content = viewPasswords.view_saved_password()
    if not content:
        messagebox.showinfo("Info", "No saved passwords found.")
        return

    win = tk.Toplevel(root)
    win.title("Saved Passwords")
    text_area = scrolledtext.ScrolledText(win, wrap=tk.WORD, width=60, height=15)
    text_area.insert(tk.END, content)
    text_area.config(state="disabled")
    text_area.pack(padx=10, pady=10)

# ------------------- SEARCH PASSWORD -------------------

def gui_search_password():
    term = search_entry.get().strip()
    if not term:
        messagebox.showerror("Error", "Enter a search term.")
        return

    matches = searchThePassword.search_password(term)

    if not matches:
        # Always show something
        win = tk.Toplevel(root)
        win.title(f"No results for '{term}'")
        text_area = scrolledtext.ScrolledText(win, wrap=tk.WORD, width=60, height=15)
        text_area.insert(tk.END, f"No passwords found for '{term}'.")
        text_area.config(state="disabled")
        text_area.pack(padx=10, pady=10)
        return

    # If matches found
    win = tk.Toplevel(root)
    win.title(f"Search Results for '{term}'")
    text_area = scrolledtext.ScrolledText(win, wrap=tk.WORD, width=60, height=15)
    text_area.insert(tk.END, "\n".join(matches))
    text_area.config(state="disabled")
    text_area.pack(padx=10, pady=10)

# ------------------- CLEAR PASSWORDS -------------------

def gui_clear_passwords():
    if messagebox.askyesno("Confirm", "Delete ALL saved passwords?"):
        deletePasswords.clear_saved_passwords()
        messagebox.showinfo("Deleted", "All saved passwords have been cleared.")

# ------------------- GUI -------------------
root = tk.Tk()
root.title("Password Manager")
root.geometry("420x450")
root.resizable(False, False)

tk.Label(root, text="Password Length:").pack(pady=2)
length_entry = tk.Entry(root)
length_entry.pack()

tk.Label(root, text="Label (e.g., Gmail, Facebook):").pack(pady=2)
label_entry = tk.Entry(root)
label_entry.pack()

tk.Button(root, text="Generate Password", command=gui_generate_password).pack(pady=5)
password_entry = tk.Entry(root, width=40)
password_entry.pack(pady=2)

tk.Button(root, text="View Saved Passwords", command=gui_view_passwords).pack(pady=5)

tk.Label(root, text="Search by Label:").pack(pady=2)
search_entry = tk.Entry(root)
search_entry.pack()
tk.Button(root, text="Search Password", command=gui_search_password).pack(pady=5)

tk.Button(root, text="Clear All Passwords", command=gui_clear_passwords).pack(pady=5)
tk.Button(root, text="Exit", command=root.destroy).pack(pady=5)

root.mainloop()
#gui_generate_password()
