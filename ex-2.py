def read_input() -> list:
    line = input().strip()
    if not line:
        return []
    return [int(i) for i in line.split()]


def remove_three(numbers: list) -> list:
    if numbers.count(3) != 1:
        raise ValueError("Исходный список должен содержать ровно одно значение 3.")
    lol = numbers.index(3)
    return numbers[:lol] + numbers[lol + 1:]


def main() -> None:
    try:
        numbers = read_input()
        result = remove_three(numbers)
        print(result)
    except ValueError as exc:
        print(exc)


if __name__ == "__main__":
    main()
