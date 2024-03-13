import tkinter as tk
import tkinter.messagebox as messagebox
import random
import string

def generate_password():
    """Generate a random password."""
    length = int(length_entry.get())
    # Define characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Shuffle the characters to ensure randomness
    shuffled_characters = random.sample(characters, len(characters))
    # Select first `length` characters to form the password
    password = ''.join(random.choices(shuffled_characters, k=length))
    password_var.set(password)

def save_password():
    """Save the password to a text file."""
    username = username_entry.get()
    password = password_var.get()
    with open("user_info.txt", "a") as file:
        file.write(f"{username},{password}\n")
    messagebox.showinfo("Success", "Password saved successfully!")

def login():
    """Login with username and password."""
    username = username_entry.get()
    password = password_entry.get()
    with open("user_info.txt", "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(',')
            if username == stored_username and password == stored_password:
                messagebox.showinfo("Success", "Login successful!")
                return
    messagebox.showerror("Error", "Invalid username or password")

def copy_to_clipboard():
    """Copy the generated password to the clipboard."""
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    root.update()
    messagebox.showinfo("Success", "Password copied to clipboard!")

# Create the main window
root = tk.Tk()
root.title("Password Generator & Login")

# Create GUI elements
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=5, pady=5)

username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=5, pady=5)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=5, pady=5)

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)

login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

signup_button = tk.Button(root, text="Sign Up", command=save_password)
signup_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=4, column=0, padx=5, pady=5)

length_entry = tk.Entry(root)
length_entry.grid(row=4, column=1, padx=5, pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

password_var = tk.StringVar()
password_label = tk.Label(root, textvariable=password_var, wraplength=200)
password_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

# Run the main event loop
root.mainloop()
