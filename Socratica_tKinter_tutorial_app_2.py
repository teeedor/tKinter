import tkinter as tk

def check_login():
    username = username_var.get()
    password = password_var.get()
    print(f"Login attempt: {username}")
    print(f"Password: {'*' * len(password)}")

def on_username_return(event):
    password_entry.focus()

def on_password_return(event):
    check_login()

root = tk.Tk()
root.title("Grid Layout Login Form")
root.geometry("400x200")

# Create StringVar Objects
username_var = tk.StringVar()
password_var = tk.StringVar()

username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=5, pady=5)

username_entry = tk.Entry(root, textvariable=username_var)
username_entry.grid(row=0, column=1, padx=5, pady=5)
username_entry.bind('<Return>', on_username_return)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=5, pady=5)

password_entry = tk.Entry(root, show="#", textvariable=password_var)
password_entry.grid(row=1, column=1, padx=5, pady=5)
password_entry.bind('<Return>', on_password_return)

login_button = tk.Button(root, text="Login", command=check_login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

# shows the power of tk.variables
mirror_label = tk.Label(root, textvariable=username_var)
mirror_label.grid(row=3, column=0, columnspan=2, pady=5)

root.mainloop()