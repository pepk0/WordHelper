from tkinter import Frame, StringVar
from tkinter import ttk


class DictFrame(Frame):
    def __init__(self) -> None:
        super().__init__()
        self.word: StringVar = StringVar()
        self.found_words = ttk.Combobox(self, values=[], state="readonly",
                                        textvariable=self.word, width=35)
        self.meaning_button = ttk.Button(self, text="Meaning", width=15)

        self.found_words.grid(row=0, column=0)
        self.meaning_button.grid(row=0, column=1)

    def set_values(self, values: list) -> None:
        self.found_words["values"] = values

    def get_word(self) -> str:
        return self.word.get()
