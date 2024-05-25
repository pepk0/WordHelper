from typing import List
import requests
from bs4 import BeautifulSoup


class Dictionary:
    CACHE = {}

    def __init__(self, word: str) -> None:
        self.word = word
        self.__word_url = f"https://rechnik.chitanka.info/w/{self.word}"

    @staticmethod
    def sanitize(text: List[str], join_by="\n") -> str:
        """Sanitizes all the words removing extra white space.
        Args:
            text (list): a list of all the sentences.
            join_by (str): the delimiter that will join all the sentences.
        Returns:
            string: the joined sentences.
        """
        new_text = []
        for word in text:
            if word:
                sanitized_word = " ".join(
                    word.strip() for word in word.split(" ") if word)
                new_text.append(sanitized_word)
        return join_by.join(new_text)

    def fetch_meaning(self) -> str:
        """Scrapes the dictionary website for the meaning of the word."""
        content = requests.get(self.__word_url).content
        soup = BeautifulSoup(content, "html.parser")
        text = soup.find("div", class_="data")
        if not text:
            text = soup.find("p", class_="data")
            if not text:
                return self.sanitize([])
            return self.sanitize(text.text.split("\n"), join_by=" ")
        return self.sanitize(text.text.split("\n"))

    def get_meaning(self) -> str:
        """Gets the meaning of a word from the cache if not present gets the 
        meaning from the web.
        Returns:
        string: the meaning of the instance word.
        """
        if self.word not in self.CACHE:
            meaning = self.fetch_meaning()
            self.CACHE[self.word] = meaning
        return self.CACHE[self.word]
