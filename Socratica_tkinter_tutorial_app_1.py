import tkinter as tk 

def process_data():
    print("click")

root = tk.Tk()
root.title("Socratica tKinter Tutorial")
root.geometry("600x400")

label = tk.Label(root, text="Teds window of great fun")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="process", command=process_data)
button.pack()

root.mainloop()