import random
from typing import List

def comb_sort(lst: List[int]) -> List[int]:
    gap = int(len(lst) / 1.3)

    while gap != 1:
        for i in range(0, len(lst)-gap):
            if lst[i] > lst[i+gap]:
                lst[i], lst[i+gap] = lst[i+gap], lst[i]
        gap = int(gap / 1.3)
    
    swap = True
    while swap:
        swap = False
        for i in range(0, len(lst)-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                swap = True

    return lst


if __name__ == '__main__':
    # lst = [2, 9, 1, 8, 7, 3, 5] 
    lst = [random.randint(0, 1000) for i in range(10)]
    print(comb_sort(lst))