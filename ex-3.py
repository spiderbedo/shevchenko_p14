import string

def words_from_sentence(sentence) -> list:
    if not sentence:
        return []

    tokens = sentence.split()
    cleaned = [token.strip(string.punctuation) for token in tokens]
    return [word for word in cleaned if word]


def main() -> None:
    sentence = input().strip()
    words = words_from_sentence(sentence)
    print(words)


if __name__ == "__main__":
    main()
