HOLES_LETTERS = set("abdegopq")


def count_holes_in_text(text) -> tuple:
    holes_count = 0
    non_holes_count = 0

    for char in text:
        if char.isalpha():
            if char in HOLES_LETTERS:
                holes_count += 1
            else:
                non_holes_count += 1

    return holes_count, non_holes_count


def words_with_multiple_holes(text) -> list:
    words = text.split()
    result = []
    for i in words:
        count = sum(1 for char in i if char in HOLES_LETTERS)
        if count >= 2:
            result.append(word)
    return result


def main() -> None:
    text = input("Введите строку: ").lower()
    holes_count, non_holes_count = count_holes_in_text(text)
    words_with_holes = words_with_multiple_holes(text)

    print(holes_count, non_holes_count)
    print(words_with_holes)


if __name__ == "__main__":
    main()
