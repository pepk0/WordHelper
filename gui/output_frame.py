from tkinter import Frame, LabelFrame, Label, END


class OutputFrame(Frame):
    def __init__(self) -> None:
        super().__init__()
        self.label_frame = LabelFrame(
            self, text="Found Words", height=74, labelanchor="n",
            borderwidth=4, font=("Helvetica", 16), border=3)
        self.sentence_entry = Label(
            self.label_frame, width=60, font=("Helvetica", 16),
            bg="systembuttonface", bd=0)

        self.label_frame.pack(pady=20)
        self.sentence_entry.pack(pady=20)

    def print(self, words) -> None:
        if isinstance(words, list):
            words = ", ".join(words)
        self.sentence_entry["text"] = words
