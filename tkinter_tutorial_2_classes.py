# this file is going to follow the tutorial part 2 for tKinter
# will focus on using classes to make applications

import tkinter as tk # standard widgets
# from tkinter import *
from tkinter import ttk # OS themed version of widgets

def main():
    # the root window in this case is called 'app'
    app = Application()
    # allows app to be interactive
    app.mainloop()

# I have watched the tutorial, now just need to get the code down here
# Application class inherits tk.Tk which is the root window
class Application(tk.Tk):
    # constructor function of the application class
    def __init__(self):
        # super calls the constructor of the class 'Application' is inherited from
        super().__init__()
        self.title("Teds Simple app")

        # calling configure methods on the self instance of the root window
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        # Create an 'InputForm' instance within the self Application
        frame = InputForm(self)
        frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        #make a second frame in the application
        frame2 = InputForm(self)
        frame2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

# Inherits ttk.Frame
class InputForm(ttk.Frame):
    # the frame class takes a tk instance as the root, in this case it is the var parent
    def __init__(self, parent):
        # running init func of the tk.Frame class with parent var as the root
        super().__init__(parent)

        # configuring columns and rows of the frame
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        # Entry field in the frame
        self.entry = ttk.Entry(self)
        self.entry.grid(row=0, column=0, sticky="ew") 

        self.entry.bind("<Return>", self.add_to_list)

        self.entry_btn = ttk.Button(self, text="Add", command=self.add_to_list)
        self.entry_btn.grid(row=0, column=1)

        self.delete_btn = ttk.Button(self, text="Clear", command=self.clear_list)
        self.delete_btn.grid(row=0, column=2)

        self.text_list = tk.Listbox(self)
        self.text_list.grid(row=1, column=0, columnspan=3, sticky="nsew")

        self.export_btn = tk.Button(self, text="Export list", command=self.export_list)
        self.export_btn.grid(row=2, column=0, columnspan=3, sticky="ew")

    # functions called by buttons
    def add_to_list(self, event=None):
        text = self.entry.get()
        if text:
            self.text_list.insert(tk.END, text)
            self.entry.delete(0, tk.END)

    def clear_list(self):
        self.text_list.delete(0, tk.END)
    def export_list(self):
        print("exporting list")
        # self.text_list.delete(0, tk.END)

# if the file is being run directly, then do this, otherwise don't run it
if __name__ == "__main__":
    main()