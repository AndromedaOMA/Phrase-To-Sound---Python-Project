import tkinter as tk
from tkinter import filedialog, Listbox, Scrollbar
from playsound import playsound
import os


def play_selected_file(event, listbox, directory):
    if listbox.curselection():
        selected_file = listbox.get(listbox.curselection()[0])
        file_path = os.path.join(directory, selected_file)
        playsound(str(file_path))


class GUI:
    def __init__(self, output_directory):
        self.root = tk.Tk()
        self.output_directory = output_directory

    def gui(self):
        self.root.geometry("500x500")
        self.root.title("Phrase_To_Sound")

        label = tk.Label(self.root, text="Choose the mp3 you wanna hear!", font=('Arial', 20))
        label.pack()

        mp3_files = [f for f in os.listdir(self.output_directory)]

        listbox = Listbox(self.root, selectmode=tk.SINGLE, font=('Arial', 14))
        listbox.pack(fill=tk.BOTH, expand=True)

        scrollbar = Scrollbar(self.root, command=listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        listbox.config(yscrollcommand=scrollbar.set)

        for file in mp3_files:
            listbox.insert(tk.END, file)

        listbox.bind("<<ListboxSelect>>", lambda event: play_selected_file(event, listbox, self.output_directory))

        self.root.mainloop()

