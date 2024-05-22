from tkinter import Frame, Entry, StringVar
from tkinter import ttk
from word_generator.word_generator import WordGenerator


class InputFrame(Frame):
    def __init__(self) -> None:
        super().__init__()
        self.length: StringVar = StringVar()
        self.lengths = [str(num) for num in
                        range(WordGenerator.MIN_WORD_LENGTH + 1,
                              WordGenerator.MAX_WORD_LENGTH + 1)]
        self.length.set(self.lengths[0])

        self.get_letters_entry = Entry(self, width=30)
        self.get_word_length = ttk.Combobox(self, textvariable=self.length,
                                            values=self.lengths)
        self.generate_button = ttk.Button(self, text="Generate", width=25)

        self.get_letters_entry.grid(row=0, column=1, padx=3)
        self.get_word_length.grid(row=0, column=0, padx=3)
        self.generate_button.grid(row=0, column=3)

    def get_letter(self) -> str:
        """Gets the letters from the letters entry frame
        Returns:
            string the letters from the entry frame
        """
        return self.get_letters_entry.get()

    def get_length(self) -> int:
        """Gets the length from the lengths' option frame
        Returns:
            integer: the chosen number from the length option frame
        """
        return int(self.length.get())
