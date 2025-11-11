def get_numbers() -> list:
    numbers = []
    for i in range(10):
        n = int(input())
        numbers.append(n)
    return numbers

def make_new_list(nums) -> list:
    new_list = []
    for i in range(1, len(nums) - 1):
        new_list.append(nums[i - 1] + nums[i + 1])
    return new_list

def main():
    numbers = get_numbers()
    result = make_new_list(numbers)
    print("Новый список:", result)

main()
