# Добавь в свою combination_sum отсечение через сортировку: отсортируй кандидатов и прерывай цикл, как только текущее число превысило остаток.
# Замерь время до и после оптимизации на [2, 3, 5, 7, 11] и цели 30.
import time


def combination_sum_with_ots(candidates, target):
    result= []

    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(current[:])
            return
        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break
            current.append(candidates[i])
            backtrack(i, current, remaining - candidates[i])
            current.pop()

    backtrack(0, [], target)
    return result

def combination_sum(candidates, target):
    result= []

    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(current[:])
            return
        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            current.append(candidates[i])
            backtrack(i, current, remaining - candidates[i])
            current.pop()

    backtrack(0, [], target)
    return result

start = time.time()
combination_sum([2, 3, 5, 7, 11], 30)
end = time.time()
print(f'Время без отсечения: {end - start}')

start = time.time()
combination_sum_with_ots([2, 3, 5, 7, 11], 30)
end = time.time()
print(f'Время с отсечением: {end - start}')
