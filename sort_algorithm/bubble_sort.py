import random

def bubble_sort(numbers: list[int]) -> list:
    limit = len(numbers)
    flag = True
    while flag:
        flag = False
        for i in range(limit-1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                flag = True
        limit -= 1
    return numbers

if __name__ == '__main__':
    numbers = [random.randint(0, 1000) for i in range(10)]
    print('Problem: ', numbers)
    print('Answer:  ', bubble_sort(numbers))
           