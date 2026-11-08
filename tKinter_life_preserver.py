# from site https://docs.python.org/3/library/tkinter.html

import tkinter as tk # standard widgets
# from tkinter import *
from tkinter import ttk # OS themed version of widgets

# make a window with labels and buttons with all different colors
# colors = Tk()
# frm = ttk.Frame(colors, padding=50)
# frm.grid()
# ttk.Label(frm, text="Red", background="red", foreground="Green").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=colors.destroy).grid(column=2, row=0)
# colors.mainloop()

# following tutorial 1 tKinter by Corey Schafer
pad_size = 10
root = tk.Tk()
root.title("Teds first tKinter App")

# function that is called on button1
# need to handle potential event input, here is it defaulted to None
def add_to_list1(event=None):
    text = entry1.get()
    if text:
        text_list1.insert (tk.END, text)
        entry1.delete(0, tk.END)

# function that is called on button2
def add_to_list2(event=None):
    # get the text from the entry2 field
    text = entry2.get()
    # if there is text
    if text:
        # insert the text at the end of the text_list
        text_list2.insert (tk.END, text)
        # remove the text that was entered from beginning of field to end of field
        entry2.delete(0, tk.END)

# controls how the columns grow in relation to each other
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)

# --- frame 1 ---
# create frame in root window
frame = ttk.Frame(root)
# add frame to grid at 0,0, make sides stick to all sides of root, with an x and y padding of 5 pix
frame.grid(row=0, column=0, sticky="nsew", padx=pad_size, pady=pad_size)

frame.columnconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)

# Text entry box 1 inside frame
entry1 = ttk.Entry(frame)
# add the box to the frame at 0,0 and stick east and west sides to edge of screen
entry1.grid(row=0, column=0, sticky="ew")

# binds enter to the add_to_list1 function
entry1.bind("<Return>", add_to_list1)

# make button1, add it to frame, give it text and link it to add_to_list1 function
entry_btn1 = ttk.Button(frame, text="Add text 1", command=add_to_list1)
# add button to frame grid at 0,1
entry_btn1.grid(row=0, column=1)

# create text list in frame
text_list1 = tk.Listbox(frame)
# add it to the grid at 1,0, make it spread two columns and stick to all sides of window
text_list1.grid(row=1, column=0, columnspan=2, sticky="nsew")

# --- frame 2 ---
frame2 = tk.Frame(root)
# add frame2 to the right of frame
frame2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

frame2.columnconfigure(0, weight=1)
frame2.rowconfigure(1, weight=1)

entry2 = tk.Entry(frame2)
entry2.grid(row=0, column=0, sticky="ew")

entry2.bind("<Return>", add_to_list2)

entry_btn2 = tk.Button(frame2, text="Add text 2", command=add_to_list2)
entry_btn2.grid(row=0, column=1)

text_list2 = tk.Listbox(frame2)
text_list2.grid(row=1, column=0, columnspan=2, sticky="nsew")

# makes the window reactionary
root.mainloop()