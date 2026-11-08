# this app will take in a .csv file
# display it in a list, then when a selection is made of a card, it will display that card, its current market price and other things

# flow of App
# window to pick with csv file to analyze
# this will load up that File into the Card analyzer


import tkinter as tk
from tkinter import ttk

import os

import csv

# choose the csv files location
# need to check os and change csv_folder path based on that
csv_folder = "./csv_folder/"
file_names = os.listdir(csv_folder)
# print(file_names)

def main():
    file_picker = csv_picker()
    file_picker.mainloop()
    # csw = Card_stats_win()
    # csw.mainloop()

# simple window to read the folder with CSVs, to be loaded into the Card_stat_win
class csv_picker(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.title("Choose a csv to analyze")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        frame = ttk.Frame(self)
        # need these lines to get frame to resize
        frame.columnconfigure(0, weight=1) 
        frame.rowconfigure(0, weight=1) 
        # add frame to row 1 column 1 of root window
        frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        # add list box and add it to the frame
        self.file_list = tk.Listbox(frame)
        self.file_list.grid(row=0, column=0, sticky="nsew")
        # populate file_list with the file names
        for file in file_names:
            self.file_list.insert(tk.END, file)

        sub_btn = tk.Button(frame, text="Analyze file", command=self.analyze_file)
        sub_btn.grid(row=1, column=0, sticky="ew")

    def analyze_file(self):
        # selected_index is the list of selected items in the box
        selected_index = self.file_list.curselection()

        if selected_index:
            chosen_file = "csv_folder/" + self.file_list.get(selected_index[0])
            print(chosen_file)
            Card_stats_win(chosen_file)
        

        

# Card list from file on left, Images and stats on right
class Card_stats_win(tk.Tk):
    def __init__(self, file):
        super().__init__()
        self.columnconfigure(0, minsize=150)
        self.title("Card stats App")

        cards = card_picker(self, file)
        cards.columnconfigure(0, weight=1) 
        cards.rowconfigure(0, weight=1) 
        # add frame to row 1 column 1 of root window
        cards.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)


class card_picker(tk.Frame):
    def __init__(self, parent, file):
        super().__init__(parent)

        self.label = tk.Label(self, text="Pick a card to analyze")
        self.label.grid(row=0, column=0, sticky="nsew")

        # create a List box that will hold all the Data from the csv
        self.card_list = tk.Listbox(self) 
        self.card_list.columnconfigure(0, weight=1) 
        self.card_list.rowconfigure(0, weight=1) 
        self.card_list.grid(row=0, column=0, sticky="nsew")

        # Reading csv file
        # populate card_list with all cards from the file
        with open(file, "r") as card_file:
            reader = csv.reader(card_file)

            next(reader) # skip header row

            for row in reader:
                print(row)
                # following line throws an error if there is an empty row
                card_name = row[0]
                self.card_list.insert(tk.END, card_name)

        # a when a selection is made in the listbox, search the images directory for a matching card image
        # display the image on the right of the list
        # display the info about the card underneath the image

# if the file is being run directly, then do this, otherwise don't run it
if __name__ == "__main__":
    main()