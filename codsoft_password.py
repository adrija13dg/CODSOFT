from tkinter import *
from random import randint

root = Tk()
root.title("Password Generator")
root.geometry("500x400")

def generate_password():
    pass_entry.delete(0, END)
    pass_len = int(entry.get())
    pass_word = ''
    for _ in range(pass_len):
        pass_word += chr(randint(33, 126))
    pass_entry.insert(0, pass_word)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(pass_entry.get())

def clear_entries():
    entry.delete(0, END)
    pass_entry.delete(0, END)

# Label Frame
lf = LabelFrame(root, text="How Many Characters?", font=("Helvetica", 16))
lf.pack(pady=20, padx=20)

# Entry for password length
entry = Entry(lf, font=("Helvetica", 16))
entry.pack(pady=10, padx=10)

# Entry for displaying the password
pass_entry = Entry(root, text="", font=("Helvetica", 16), bd=0, bg="systembuttonface")
pass_entry.pack(pady=20)

# Frame for buttons
button_frame = Frame(root)
button_frame.pack(pady=20)

# Generate password button
generate_button = Button(button_frame, text="Generate Strong Password", font=("Helvetica", 16), command=generate_password)
generate_button.grid(row=0, column=0, padx=10)

# Copy to clipboard button
clip_button = Button(button_frame, text="Copy To Clipboard", font=("Helvetica", 16), command=copy_to_clipboard)
clip_button.grid(row=0, column=1, padx=10)

# Clear entries button
clear_button = Button(button_frame, text="Clear Entries", font=("Helvetica", 16), command=clear_entries, fg="red")
clear_button.grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()



