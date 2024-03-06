import os


def main() -> None:
    total_words_path = os.path.join("base", "words.txt")

    curr_length = 1
    with open(total_words_path, "r", encoding="utf-8") as text_file:
        for word in text_file:
            word = word.strip()
            if "-" in word:
                continue

            if len(word) > curr_length:
                print(f"-- {len(word)} length words -- Finished! --")
                curr_length = len(word)
                out_file_path = f"{curr_length}_length_words.txt"

            with open(out_file_path, "a", encoding="utf-8") as new_file:
                new_file.write(word + "\n")


if __name__ == "__main__":
    main()
