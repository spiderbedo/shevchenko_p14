def read_numbers() -> list:
    line = input("Введите целые числа через пробел: ").strip()
    if not line:
        return []
    return [int(token) for token in line.split()]


def average(numbers) -> float:
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def main() -> None:
    try:
        numbers = read_numbers()
        result = average(numbers)
        print("Среднее значение элементов списка:", result)
    except ValueError as exc:
        print(exc)


if __name__ == "__main__":
    main()
