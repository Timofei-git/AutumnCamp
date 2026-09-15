# Напиши функцию find_unique(nums), которая находит единственное неповторяющееся число в списке, где все остальные встречаются дважды. Реши через XOR за O(1) памяти.

def find_unique(lst):
    result = 0
    for num in lst:
        result ^= num
    return result

print(find_unique([4, 1, 2, 1, 2]))
