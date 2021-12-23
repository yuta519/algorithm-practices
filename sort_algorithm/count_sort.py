import random


def couting_sort(original_array: list[int]) -> list[int]:
    max_num: int = max(original_array)
    count_array: list[int] = [original_array.count(i) for i in range(0, max_num + 1)]

    calculated_array: list[int] = []
    base_int: int = 0
    for i in count_array:
        base_int += i
        calculated_array.append(base_int)

    sorted_array: list[int] = [i for i in range(0, len(original_array))]
    for i in reversed(original_array):
        sorted_array[calculated_array[i] - 1] = i
        calculated_array[i] -= 1
    return sorted_array


if __name__ == "__main__":
    test_array: list[int] = [4, 3, 6, 2, 3, 4, 7]
    print(couting_sort(test_array))
    nums: list[int] = [random.randint(0, 10000) for _ in range(10)]
    print(couting_sort(nums))
