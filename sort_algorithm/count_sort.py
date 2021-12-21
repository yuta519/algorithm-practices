def couting_sort(original_array: list[int]) -> list[int]:
    max_num: int = max(original_array)
    count_array: list[int] = [original_array.count(i) for i in range(0, max_num + 1)]
    return count_array
    # index_num: int = max_num
    # while index_num >= 0:
    #     if count_array[index_num] != 0:
    #         index_num: int = index_num - 1


if __name__ == "__main__":
    test_array: list[int] = [4, 3, 6, 2, 3, 4, 7]
    print(couting_sort(test_array))
