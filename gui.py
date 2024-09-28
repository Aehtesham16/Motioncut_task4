import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length, use_uppercase, use_numbers, use_symbols):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def copy_to_clipboard(password):
    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Copied", "Password copied to clipboard!")

def generate():
    try:
        length = int(length_entry.get())
        use_uppercase = uppercase_var.get()
        use_numbers = numbers_var.get()
        use_symbols = symbols_var.get()

        password = generate_password(length, use_uppercase, use_numbers, use_symbols)
        result_label.config(text=f"Generated Password: {password}")
        
        copy_button.config(state="normal", command=lambda: copy_to_clipboard(password))

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the length.")

# GUI setup
root = tk.Tk()
root.title("Secure Password Generator")

tk.Label(root, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

uppercase_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var).pack(pady=5)
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack(pady=5)
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate)
generate_button.pack(pady=10)

result_label = tk.Label(root, text="Generated Password: ")
result_label.pack(pady=10)

copy_button = tk.Button(root, text="Copy to Clipboard", state="disabled")
copy_button.pack(pady=5)

# Start the GUI
root.mainloop()
