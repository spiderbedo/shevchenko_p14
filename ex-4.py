import string

def words_from_sentence(sentence) -> list:
    if not sentence:
        return []

    tokens = sentence.split()
    unique_words = []
    lol = set()

    for token in tokens:
        word = token.strip(string.punctuation).lower()
        if word and word not in lol:
            unique_words.append(word)
            lol.add(word)

    return unique_words


def main() -> None:
    sentence = input().strip()
    words = words_from_sentence(sentence)
    print(words)


if __name__ == "__main__":
    main()
