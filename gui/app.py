import tkinter as tk
from tkinter import ttk
from word_generator.word_generator import WordGenerator


class App(tk.Tk):
    def __init__(self, ):
        super().__init__()
        self.title("Word Helper")
        self.geometry("700x200")
        self.resizable(False, False)

        def get_words() -> None:
            """Gets the validated words and presents them on the frame."""
            try:
                word_generator = WordGenerator(get_letters_entry.get(),
                                               int(length.get()))
                found_words = word_generator.get_valid_words()
                print(found_words)
            except (ValueError, FileNotFoundError) as exception:
                found_words = exception

            sentence_entry.delete(0, tk.END)
            sentence_entry.insert(0, found_words)

        # output frame for valid words
        label_frame = tk.LabelFrame(
            self, text="Found Words", height=74, labelanchor="n",
            borderwidth=4, font=("Helvetica", 16), border=3)
        # output words will be shown in this frame
        sentence_entry = tk.Entry(
            label_frame, width=60, font=("Helvetica", 14),
            bg="systembuttonface", bd=0)

        lengths = ["3", "4", "5", "6"]
        length = tk.StringVar()
        length.set(lengths[0])

        # input parameter will be stored in this frame
        get_info_label = tk.Frame(self)
        get_letters_entry = tk.Entry(get_info_label, width=30, )
        get_word_length = ttk.Combobox(
            get_info_label, textvariable=length, values=lengths)
        generate_button = ttk.Button(
            get_info_label, text="Generate", command=get_words, width=25)

        # placement of the widgets in on the app frame
        label_frame.pack(pady=20)
        sentence_entry.pack(pady=20)
        get_info_label.pack(pady=3)
        get_letters_entry.grid(row=0, column=1, padx=3)
        get_word_length.grid(row=0, column=0, padx=3)
        generate_button.grid(row=0, column=3)
