import requests
from bs4 import BeautifulSoup


class Dictionary:
    CACHE = {}

    def __init__(self, word: str) -> None:
        self.word = word
        self.__word_url = f"https://rechnik.chitanka.info/w/{self.word}"

    @staticmethod
    def sanitize(text: list) -> list:
        new_text = []
        for word in text:
            if word:
                new_text.append(word.strip())
        return new_text

    def fetch_meaning(self) -> list | str:
        content = requests.get(self.__word_url).content
        soup = BeautifulSoup(content, "html.parser")
        try:
            text = soup.find("div", class_="data").text.split("\n")
            return self.sanitize(text)
        except AttributeError:
            return f"Няма намерено значенине на думата: {self.word}!"

    def get_meaning(self) -> str:
        if self.word not in self.CACHE:
            meaning = self.fetch_meaning()
            self.CACHE[self.word] = meaning
        return self.CACHE[self.word]
