def couting_sort(original_array: list[int]) -> list[int]:
    max_num: int = max(original_array)
    count_array: list[int] = [original_array.count(i) for i in range(0, max_num + 1)]
    calculated_array: list[int] = []
    base_int: int = 0
    for i in count_array:
        base_int += i
        calculated_array.append(base_int)
    return calculated_array


if __name__ == "__main__":
    test_array: list[int] = [4, 3, 6, 2, 3, 4, 7]
    print(couting_sort(test_array))
