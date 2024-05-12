from tkinter import Toplevel, Label


class MeaningFrame(Toplevel):
    def __init__(self, parent, text: str) -> None:
        super().__init__(parent)
        self.text = text
        self.parent = parent
        self.resizable(False, False)
        self.title("Word Meaning")
        self.text_frame = Label(self, text="\n".join(text),
                                font=("Consolas", 15), justify="left",
                                wraplength=600)
        self.text_frame.grid(row=0, column=0)
