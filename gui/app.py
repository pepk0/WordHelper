import tkinter as tk
from Wordy.utils.functionality import validate_words
from tkinter import ttk


class App(tk.Tk):
    def __init__(self,):
        super().__init__()
        self.title("Word Helper")
        self.geometry("700x200")
        self.resizable(False, False)
        self.cache = {}

        def get_words() -> None:
            # get the desired length of the output words and letter sequence
            words_length = int(length.get())
            word_sequence = get_letters_entry.get()
            found_words = validate_words(
                self.cache, word_sequence, words_length)
            sentence_entry.delete(0, tk.END)
            sentence_entry.insert(0, found_words)

        # output frame for found words
        label_frame = tk.LabelFrame(
            self, text="Found Words", height=74, labelanchor="n",
            borderwidth=4, font=("Helvetica", 16), border=3)
        # output words will be shown here
        sentence_entry = tk.Entry(
            label_frame, width=60, font=("Helvetica", 14),
            bg="systembuttonface", bd=0)

        lengths = ["3", "4", "5", "6"]
        length = tk.StringVar()
        length.set(lengths[0])
        # input parameter will be stored in this frame
        get_info_label = tk.Frame(self)
        get_letters_entry = tk.Entry(get_info_label, width=30,)
        get_word_length = ttk.Combobox(
            get_info_label, textvariable=length, values=lengths)
        generate_button = ttk.Button(
            get_info_label, text="Generate", command=get_words, width=25)

        label_frame.pack(pady=20)
        sentence_entry.pack(pady=20)
        get_info_label.pack(pady=3)
        get_letters_entry.grid(row=0, column=1, padx=3)
        get_word_length.grid(row=0, column=0, padx=3)
        generate_button.grid(row=0, column=3)
