import tkinter as tk
from tkinter import ttk
from word_generator.word_generator import WordGenerator


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Word Helper")
        self.geometry("700x200")
        self.resizable(False, False)

        # output frame for valid words
        self.label_frame = tk.LabelFrame(
            self, text="Found Words", height=74, labelanchor="n",
            borderwidth=4, font=("Helvetica", 16), border=3)
        # output words will be shown in this frame
        self.sentence_entry = tk.Entry(
            self.label_frame, width=60, font=("Helvetica", 14),
            bg="systembuttonface", bd=0)

        # dynamically generates all the valid word lengths from min to max,
        # set in the WordGenerator class
        self.lengths = [str(num) for num in
                        range(WordGenerator.MIN_WORD_LENGTH + 1,
                              WordGenerator.MAX_WORD_LENGTH + 1)]
        self.length = tk.StringVar()
        self.length.set(self.lengths[0])

        # input parameter will be stored in this frame
        self.get_info_label = tk.Frame(self)
        self.get_letters_entry = tk.Entry(self.get_info_label, width=30, )
        get_word_length = ttk.Combobox(
            self.get_info_label, textvariable=self.length, values=self.lengths)
        generate_button = ttk.Button(
            self.get_info_label, text="Generate", command=self.get_words,
            width=25)

        # placement of the widgets in on the app frame
        self.label_frame.pack(pady=20)
        self.sentence_entry.pack(pady=20)
        self.get_info_label.pack(pady=3)
        self.get_letters_entry.grid(row=0, column=1, padx=3)
        get_word_length.grid(row=0, column=0, padx=3)
        generate_button.grid(row=0, column=3)

    def get_words(self) -> None:
        """Gets the validated words and presents them on the frame."""
        try:
            word_generator = WordGenerator(self.get_letters_entry.get(),
                                           int(self.length.get()))
            found_words = word_generator.get_valid_words()
        except (ValueError, FileNotFoundError) as exception:
            found_words = exception

        self.sentence_entry.delete(0, tk.END)
        self.sentence_entry.insert(0, found_words)
