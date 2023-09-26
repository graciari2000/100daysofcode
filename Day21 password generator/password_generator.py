import tkinter as tk
import random
import string

def generate_password():
    password_length = int(length_entry.get())
    use_uppercase = uppercase_var.get()
    use_digits = digits_var.get()
    use_special_chars = special_chars_var.get()

    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(password_length))
    password_result.config(text=password)

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Labels
length_label = tk.Label(window, text="Password Length:")
length_label.pack()

# Entry for password length
length_entry = tk.Entry(window)
length_entry.pack()

# Checkboxes for character options
uppercase_var = tk.BooleanVar()
uppercase_check = tk.Checkbutton(window, text="Uppercase", variable=uppercase_var)
uppercase_check.pack()

digits_var = tk.BooleanVar()
digits_check = tk.Checkbutton(window, text="Digits", variable=digits_var)
digits_check.pack()

special_chars_var = tk.BooleanVar()
special_chars_check = tk.Checkbutton(window, text="Special Characters", variable=special_chars_var)
special_chars_check.pack()

# Button to generate password
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

# Display the generated password
password_result = tk.Label(window, text="", wraplength=300)
password_result.pack()

# Start the GUI
window.mainloop()