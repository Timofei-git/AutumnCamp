# Напиши функцию find_all(text, pattern), возвращающую список всех индексов вхождений, включая перекрывающиеся. Проверь на "abababa" и "aba" — ответ [0, 2, 4].

def find_all(text, pattern):
    result = []
    t = len(text)

    for i in range(t - len(pattern) + 1):
        j = 0

        while j < len(pattern) and pattern[j] == text[i + j]:
            j += 1

        if j == len(pattern):
            result.append(i)

    return result

print(find_all("abababa", "aba"))