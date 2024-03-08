import os


def main() -> None:
    # the base words file containing all the words in one place
    total_words_path = os.path.join("base", "words.txt")

    curr_word_length = 1
    with open(total_words_path, "r", encoding="utf-8") as text_file:
        for word in text_file:
            # removes the newline after the word
            word = word.strip()

            # words containing dashes are not present in the game
            if "-" in word:
                continue

            if len(word) > curr_word_length:
                print(f"-- {len(word)} length words -- Done! --")
                curr_word_length = len(word)
                out_file = f"{curr_word_length}_length_words.txt"
                # clears previous files with this length
                with open(out_file, "w", encoding="utf-8"):
                    continue

            # puts all the words in the specific length file
            with open(out_file, "a", encoding="utf-8") as new_file:
                new_file.write(word + "\n")


if __name__ == "__main__":
    main()
