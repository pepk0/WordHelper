import requests
from bs4 import BeautifulSoup


class Dictionary:
    CACHE = {}

    def __init__(self, word: str) -> None:
        self.word = word
        self.__word_url = f"https://rechnik.chitanka.info/w/{self.word}"

    def fetch_meaning(self) -> str:
        content = requests.get(self.__word_url).content
        soup = BeautifulSoup(content, "html.parser")
        try:
            return soup.find("div", class_="data").text.strip()
        except AttributeError:
            return f"Няма намерено значенине на думата: {self.word}!"

    def get_meaning(self) -> str:
        if self.word not in self.CACHE:
            meaning = self.fetch_meaning()
            self.CACHE[self.word] = meaning
        return self.CACHE[self.word]
