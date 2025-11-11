def sort_string_characters(text) -> str:
    chars = list(text)      
    chars.sort()          
    sorted_text = ''.join(chars)  
    return sorted_text


def main() -> None:
    text = input("Введите строку: ")
    result = sort_string_characters(text)
    print("Отсортированная строка:", result)


if __name__ == "__main__":
    main()
