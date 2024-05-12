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
        """Sets the values to the option list
        Args:
            values: list containing all the values to be added
        """
        self.found_words["values"] = values

    def get_word(self) -> str:
        """Gets the word chosen from the option list
        Returns:
            string: the word chosen from the list frame
        """
        return self.word.get()
