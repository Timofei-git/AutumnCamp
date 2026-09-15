# Напиши функцию subsets(nums), возвращающую все подмножества списка. Для [1, 2, 3] должно получиться 8 подмножеств, включая пустое.

def permutations(nums):
    result = []

    def backtrack(start, current):
        result.append(current[:])

        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i+1, current)
            current.pop()

    backtrack(0, [])

    return result

print(permutations([1,2,3]))