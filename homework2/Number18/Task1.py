# Напиши функцию permutations(nums), генерирующую все перестановки списка. Проверь на [1, 2, 3] — должно получиться 6 вариантов.
from itertools import permutations


def permutations(nums):
    result = []

    def backtrack(current, remaining):

        if not remaining:
            result.append(current[:])
            return

        for i in range(len(remaining)):
            current.append(remaining[i])
            backtrack(current, remaining[:i] + remaining[i+1:])
            current.pop()

    backtrack([], nums)

    return result

print(permutations([1,2,3]))