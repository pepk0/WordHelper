import tkinter as tk
from gui.input_frame import InputFrame
from word_generator.word_generator import WordGenerator
from gui.output_frame import OutputFrame
from gui.meaning_frame import MeaningFrame
from gui.dictionary_frame import DictFrame
from dictionary.dictionary import Dictionary


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Word Helper")
        self.geometry("700x200")
        self.resizable(False, False)
        self.output_frame = OutputFrame()
        self.input_frame = InputFrame()
        self.dictionary = DictFrame()

        # adding functionality to the buttons
        self.input_frame.generate_button["command"] = self.get_words
        self.dictionary.meaning_button["command"] = self.get_meaning

        # placement of the widgets in on the app frame
        self.output_frame.pack()
        self.input_frame.pack(pady=3)
        self.dictionary.pack(pady=3)

    def get_words(self) -> None:
        """Gets the validated words and presents them."""
        self.dictionary.found_words.set("")
        letters = self.input_frame.get_letter()
        word_length = self.input_frame.get_length()
        try:
            word_generator = WordGenerator(letters, word_length)
            found_words = word_generator.get_valid_words()
            self.dictionary.set_values(found_words)
        except (ValueError, FileNotFoundError) as exception:
            found_words = exception

        self.output_frame.print(found_words)

    def get_meaning(self) -> None:
        """Opens a new window contain the information 
        for the word in the choice box"""
        word = self.dictionary.get_word()
        if not word:
            return
        word_meaning = Dictionary(word).get_meaning()
        if not word_meaning:
            word_meaning = f"Няма намерена информация за думата {word}"
        # opens up a new window containing the text meaning of the word
        MeaningFrame(self, word_meaning)
