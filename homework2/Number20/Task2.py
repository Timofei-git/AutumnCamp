# Напиши функцию count_occurrences(text, pattern), которая считает количество непересекающихся вхождений подстроки, и сравни результат со встроенным методом count.

def naive_search(text, pattern):
    t = len(text)

    for i in range(t - len(pattern) + 1):
        j = 0

        while j < len(pattern) and pattern[j] == text[i + j]:
            j += 1

        if j == len(pattern):
            return i

    return -1

def count_occurrences(text, pattern):
    count = 0
    t = len(text)
    i = 0
    while i < t - len(pattern) + 1:
        pos = naive_search(text[i:], pattern)
        if pos == -1:
            return count

        count += 1
        i = i + pos + len(pattern)

    return count

print(f'Результаты моей функции: {count_occurrences("bbaaaaaa", "aa")}')
print(f'Результаты функции count: {'bbaaaaaa'.count('aa')}')
# Результаты получаются одинаковыми