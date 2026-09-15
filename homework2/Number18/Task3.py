# Напиши функцию, которая генерирует все возможные строки из n открывающих и n закрывающих скобок (без проверки на правильность). Для n = 2 получится 6 вариантов длины 4.
lst = '()'
def permutations(lst, n):
    result = set()

    def backtrack(current, remaining):

        if not remaining:
            result.add(current)
            return

        for i in range(len(remaining)):
            backtrack(current + remaining[i], remaining[:i] + remaining[i+1:])
            
    backtrack('', lst * n)

    return set(result)


print(permutations(lst, 2))