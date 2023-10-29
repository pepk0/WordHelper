from itertools import permutations


def get_words(characters: str, digits: int) -> list:
    """Takes a sequence of characters and a length, 
    returns a list if all  permutations.
    """
    letter_combinations = permutations(characters, digits)
    result = ["".join(word) for word in letter_combinations]
    return result


def validate_words(prev_searches: dict, characters: str, length: int) -> str:
    """Validates sequence of letters.
    
    arguments:
    prev_searches -- dictionary, storing previous results of this function
    characters -- sequence of letters 
    length -- length of desired word validations
    returns: 
    string of all validated words matching the arguments
    """
    if len(characters) == 0 or len(characters) < length:
        return "You need more Cyrillic letters"
    # If a number that is more than the range, 
    # length set to 3 letters
    if length < 3 or length > 6:
        length = 3
    # check our previous queries
    if (characters, length) in prev_searches:
        return prev_searches[(characters, length)]
    else:  # no cached results for our query
        result = ""
        words = get_words(characters, length)
        try:
            with open(r"words.txt", "r", encoding="utf-8") as txt_file:
                for word in txt_file:
                    word = word.strip()
                    if word in words:
                        result += f"{word} "
        except FileNotFoundError:
            result = "Missing words.txt, or path for words.txt is incorrect"
            return result
        # Add the query to the cache before returning it
        prev_searches[(characters, length)] = result
        return prev_searches[(characters, length)]
