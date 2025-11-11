import string


def read_text() -> str:
    print("Введите текст:")
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    return " ".join(lines)


def get_words(text) -> list:
    words = []
    for token in text.split():
        word = token.strip(string.punctuation).lower()
        if word:
            words.append(word)
    return words


def sort_words_by_frequency(words) -> list:
    frequency = {}
    order = {}

    for index, word in enumerate(words):
        frequency[word] = frequency.get(word, 0) + 1
        if word not in order:
            order[word] = index

    sorted_words = sorted(frequency.keys(),\
                          key=lambda w: (-frequency[w], order[w]))
    return sorted_words


def main() -> None:
    text = read_text()
    words = get_words(text)
    sorted_words = sort_words_by_frequency(words)
    for i in sorted_words:
        print(i)


if __name__ == "__main__":
    main()
