import time  #  Составь текст из 10000 одинаковых букв «a» и образец из 100 букв «a» с буквой «b» в конце.
 #  Замерь время работы своей наивной функции и встроенного оператора in, выведи обе цифры и объясни разницу в комментарии.

def naive_search(text, pattern):
    t = len(text)

    for i in range(t - len(pattern) + 1):
        j = 0

        while j < len(pattern) and pattern[j] == text[i + j]:
            j += 1

        if j == len(pattern):
            return i

    return -1

text = 'a' * 10000
pattern = 'a' * 100 + 'b'
start = time.time()
result = naive_search(text, pattern)
print(result)
print(f'Время выполнения наивной функции: {time.time() - start}')

start = time.time()
result = pattern in text
print(result)
print(f'Время выполнения наивной функции: {time.time() - start}')

