# Напиши функцию naive_search(text, pattern), которая возвращает индекс первого вхождения подстроки или -1. Не используй find, index и оператор in.

def naive_search(text, pattern):
    t = len(text)

    for i in range(t - len(pattern) + 1):
        j = 0

        while j < len(pattern) and pattern[j] == text[i + j]:
            j += 1

        if j == len(pattern):
            return i

    return -1

test_cases = [
    ("hello world", "world"),
    ("hello world", "hello"),
    ("abcabcabc", "cab"),
    ("hello world", "xyz")

]
for test, string in test_cases:
    print(naive_search(test, string))