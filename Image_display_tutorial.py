import tkinter as tk
from tkinter import filedialog
import csv

# this seems to be working, Learn from this to make changes to your own Project
class CSVImageViewer:

    def __init__(self, root):
        self.root = root
        self.root.title("CSV Image Viewer")
        self.root.geometry("900x800")

        # Store csv Entries
        self.csv_data = []

        # keep reference to current image
        self.current_image = None

        # Main container
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill="both", expand=True, padx=5, pady=5)

        # Listbox on the left
        self.listbox = tk.Listbox(
            self.main_frame,
            width=30,
            height=25
        )
        self.listbox.pack(side="left", fill="y")

        # Detect when an item is selected
        self.listbox.bind(
            "<<ListboxSelect>>",
            self.display_image
        )

        # Image display on the right
        self.image_label = tk.Label(
            self.main_frame,
            text="Select an Entry"
        )
        self.image_label.pack(
            side="left",
            fill="both",
            expand=True,
            padx=20
        )

        # Button to load CSV
        self.load_button = tk.Button(
            root,
            text="Load CSV",
            command=self.load_csv
        )
        self.load_button.pack(pady=10)

    def load_csv(self):

        file_path = filedialog.askopenfilename(
            filetypes=[("CSV Files", "*.csv")]
        )

        if not file_path:
            return

        self.csv_data.clear()
        self.listbox.delete(0, tk.END)

        with open(file_path, "r", newline="", encoding="utf-8-sig") as file:

            reader = csv.DictReader(file)

            for row in reader:
                self.csv_data.append(row)
                
                # add card name to listbox
                self.listbox.insert(
                    tk.END,
                    row["name"]
                )
    def display_image(self, event):

        # get selected Listbox index
        selection = self.listbox.curselection()

        if not selection:
            return

        index = selection[0]

        # retrieve corresponding csv entry
        selected_entry = self.csv_data[index]

        # get image path
        image_path = selected_entry["ImagePath"]

        try:
            # Load image using native tKinter
            self.current_image = tk.PhotoImage(
                file=image_path
            )

            # Display image
            self.image_label.config(
                image=self.current_image,
                text=""
            )

        except tk.TclError as error:

            self.image_label.config(
                image="",
                text=f"Could not load image : \n{error}"
            )

root = tk.Tk()

app = CSVImageViewer(root)

root.mainloop()