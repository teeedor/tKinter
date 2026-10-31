# from site https://docs.python.org/3/library/tkinter.html

from tkinter import *
from tkinter import ttk

# # Basic window with button
# # create a main window for the application
# root = Tk()
# # create a frame within the main window to hold the widgets with padding some number
# frm = ttk.Frame(root, padding=30)
# # frame has a grid layout
# frm.grid()
# # Label on the left
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# # Button on the right to call the destroy method
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# # this actually renders the output
# root.mainloop()

# make a second window to see what happens when I run it, it runs after the first window is closed
# scoot = Tk()
# frm = ttk.Frame(scoot, padding=30)
# frm.grid()
# ttk.Label(frm, text="Goodbye World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=scoot.destroy).grid(column=1, row=0)
# scoot.mainloop()

# make a window with labels and buttons with all different colors
colors = Tk()
frm = ttk.Frame(colors, padding=50)
frm.grid()
ttk.Label(frm, text="Red", background="red", foreground="Green").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=colors.destroy).grid(column=2, row=0)
colors.mainloop()