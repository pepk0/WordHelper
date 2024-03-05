import os

from itertools import permutations


class WordGenerator:
    MAX_WORD_LENGTH = 6
    MIN_WORD_LENGTH = 1

    def __init__(self, letters: str, word_length: int) -> None:
        self.word_length = word_length
        self.letters = letters
        self.cache: dict = {}
        self.valid_words_list = os.path.join("valid_words", "words.txt")

    @property
    def letters(self) -> str:
        return self.__letters

    @letters.setter
    def letters(self, letters: str) -> None:
        if not letters:
            raise ValueError("Please enter some letters!")
        elif not self.MIN_WORD_LENGTH < len(letters) <= self.MAX_WORD_LENGTH:
            raise ValueError(f"Invalid letters length "
                             f"between ({self.MIN_WORD_LENGTH} "
                             f"- {self.MAX_WORD_LENGTH})")
        elif self.word_length > len(letters):
            raise ValueError(f"Cant make {self.word_length} letter word "
                             f"with {len(letters)} provided letters")

        self.__letters = letters

    @property
    def word_length(self) -> int:
        return self.__word_length

    @word_length.setter
    def word_length(self, word_length: int) -> None:
        if not self.MIN_WORD_LENGTH < word_length <= self.MAX_WORD_LENGTH:
            raise ValueError("Invalid length!")
        self.__word_length = word_length

    def get_words(self) -> set:
        """Takes a sequence of characters and a length, and
        returns a set if all  permutations."""
        letter_combinations = permutations(self.letters, self.word_length)
        word_combinations = {"".join(word) for word in letter_combinations}
        return word_combinations

    def get_validate_words(self) -> str:
        """"Loops through the valid words list checking if any word is in the
        permutation set if present the word is added to the result"""
        # check our previous queries
        if (self.letters, self.word_length) not in self.cache:
            result = ""
            words = self.get_words()
            try:
                with open(self.valid_words_list, "r", encoding="utf-8") as f:
                    for word in f:
                        word = word.strip()
                        if len(word) > self.word_length:
                            break
                        if word in words:
                            result += f"{word} "
            except FileNotFoundError:
                result = "Missing words.txt"
                return result
            # Add the query to the cache before returning it
            self.cache[(self.letters, self.word_length)] = result

            return self.cache[(self.letters, self.word_length)]
