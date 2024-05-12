import tkinter as tk
from tkinter import ttk

from gui.input_frame import InputFrame
from word_generator.word_generator import WordGenerator
from gui.output_frame import OutputFrame


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Word Helper")
        self.geometry("700x200")
        self.resizable(False, False)
        self.output_frame = OutputFrame()
        self.input_frame = InputFrame()

        # adding function to the button
        self.input_frame.generate_button["command"] = self.get_words

        # placement of the widgets in on the app frame
        self.output_frame.pack()
        self.input_frame.pack(pady=3)

    def get_words(self) -> None:
        """Gets the validated words and presents them."""
        letters = self.input_frame.get_letter()
        word_length = self.input_frame.get_length()
        try:
            word_generator = WordGenerator(letters, word_length)
            found_words = word_generator.get_valid_words()
        except (ValueError, FileNotFoundError) as exception:
            found_words = exception

        self.output_frame.print(found_words)
