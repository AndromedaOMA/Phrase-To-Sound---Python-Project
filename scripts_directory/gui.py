import tkinter as tk
from gtts import gTTS
# from tkinter import filedialog, Listbox, Scrollbar, messagebox
from tkinter import Listbox, messagebox
from playsound import playsound
import os
# from .converter import Converter
# from scripts_directory import Converter


def play_selected_file(listbox, directory):
    if listbox.curselection():
        selected_file = listbox.get(listbox.curselection()[0])
        file_path = os.path.join(directory, selected_file).replace("\\", "/")
        playsound(str(file_path))


def play_text_as_audio_from_btn(text):
    if not text.strip():
        messagebox.showwarning("Warning!", "Insert a quote!")
        return

    gtts = gTTS(text=text, lang='en')
    gtts.save('audio_quote.mp3')
    playsound('audio_quote.mp3')
    os.remove('audio_quote.mp3')


class GUI:
    def __init__(self, output_directory):
        self.root = tk.Tk()
        self.output_directory = output_directory

    def gui(self):
        self.root.geometry("700x700")
        self.root.title("Phrase_To_Sound")

        label = tk.Label(self.root, text="Choose the mp3 you wanna hear or add a new quote!", font=('Arial', 20))
        label.pack()

        mp3_files = [f for f in os.listdir(self.output_directory)]
        listbox = Listbox(self.root, selectmode=tk.SINGLE, font=('Arial', 25))
        listbox.pack(fill=tk.BOTH, expand=True)
        for file in mp3_files:
            listbox.insert(tk.END, file)
        listbox.bind("<<ListboxSelect>>", lambda event: play_selected_file(listbox, self.output_directory))

        entry = tk.Entry(self.root, width=50)
        entry.pack(fill=tk.BOTH, expand=True)

        # c = Converter('', '')
        button = tk.Button(self.root, text="Play!",  font=('Arial', 25),
                           command=lambda: play_text_as_audio_from_btn(entry.get()))
        button.pack(fill=tk.BOTH, expand=True)

        self.root.mainloop()
