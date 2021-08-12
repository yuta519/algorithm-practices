import random

def cocktail_sort(lst: list[int]) -> list[int]:
    swap =  True
    limit = [0, len(lst)-1]
    while swap:
        swap = False
        for i in range(limit[0], limit[1]):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                swap = True
        limit[1] = limit[1]-1
        if swap == True:
            # alternative 
            # for i in range(limit[0], limit[1], -1):
            for i in reversed(range(limit[0]+1, limit[1]-1)):
                if lst[i-1] > lst[i]:
                    lst[i], lst[i-1] = lst[i-1], lst[i]
                    swap = True
            limit[0] = limit[0]+1
    return lst

if __name__ == '__main__':
    nums = [random.randint(0, 1000) for i in range(10)]
    print(nums)
    print(cocktail_sort(nums))