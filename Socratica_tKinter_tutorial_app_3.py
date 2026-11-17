import tkinter as tk
from tkinter import ttk

def submit_landing_request():
    print(f"Landing Site Selected: {site_var.get()}")
    print(f"Visit Purpose: {purpose_var.get()}")
    print(f"Experience: {experience_var.get('1.0', tk.END)}")
    print(f"Rover Protection: {rover_var.get()}")
    print(f"Mars Time Accepted: {time_var.get()}")

root = tk.Tk()
root.title("Mars Surface Control - Landing Permit Application")
root.geometry("600x500")

# Variables

site_var = tk.StringVar()
purpose_var = tk.IntVar()
experience_var = tk.BooleanVar()
time_var = tk.BooleanVar()

# Landing Sites
site_label = ttk.Label(root, text="Intended Landing Site:")
site_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')

landing_sites = [
    "Olympus Mons Base Alpha",
    "Valles Marineris Research Station",
    "Rover Battle Stadium",
    "Hellas Impact Basic Resort"
]

site_combo = ttk.Combobox(root, textvariable=site_var, values=landing_sites, width=30)
site_combo.grid(row=1, column=0, padx=5, pady=5, sticky='w')
site_combo.set("Select Landing Site")

# Visit Purpose
purpose_label = tk.Label(root, text="Purpose of Visit:")
purpose_label.grid(row=2, column=0, padx=5, pady=5, sticky='w')

purposes = [
    ("Terraforming Work Permit", 1),
    ("Red Planet Tourism", 2),
    ("Martian University Studies", 3),
    ("Definitely Not Earth Invasion", 4)
]

for i, (text, value) in enumerate(purposes):
    rb = ttk.Radiobutton(root, text=text, value=value, variable=purpose_var)
    rb.grid(row=i+3, column=0, padx=20, pady=2, sticky='w')

# Experience Text Area
experience_label = ttk.Label(root,
                             text="Please explain your experience with low gravity environments:")
experience_label.grid(row=8, column=0, padx=5, pady=5, sticky='w')

experience_text = tk.Text(root, height=4, width=50)
experience_text.grid(row=9, column=0, padx=5, pady=5)

# Required Declarations
declaration_label = ttk.Label(root, text="Required Declarations", font=('Arial', 10, 'bold'))
declaration_label.grid(row=10, column=0, padx=5, pady=10, sticky='w')

# Need to keep working on this later