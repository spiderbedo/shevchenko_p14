import math

def find_divisors(num):
    divisors = set()  
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            divisors.add(i)
            divisors.add(num // i)  
    return list(divisors)


def main() -> None:
    try:
        num = int(input("Введите целое число: "))
        result = find_divisors(num)
        print("Делители:", result)
    except ValueError as exc:
        print(exc)


if __name__ == "__main__":
    main()
