def read_numbers() -> list:
    line = input(" ").strip()
    if not line:
        return []
    return [int(lol) for lol in line.split()]


def sum_even_odd(numbers) -> tuple:
    even_sum = 0
    odd_sum = 0
    for i in numbers:
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i
    return even_sum, odd_sum


def main() -> None:
    try:
        numbers = read_numbers()
        even_sum, odd_sum = sum_even_odd(numbers)
        print("Сумма чётных чисел:", even_sum)
        print("Сумма нечётных чисел:", odd_sum)
    except ValueError as exc:
        print(exc)


if __name__ == "__main__":
    main()
