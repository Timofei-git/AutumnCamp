#  3 задание Напиши функцию is_anagram(a, b), проверяющую два слова на анаграммы через сортировку букв. Проверь на «рост» и «сорт».

# 4 задание Напиши вторую версию is_anagram без сортировки — через подсчёт количества каждой буквы.
# Сравни время работы обеих версий на строках длиной 100 000 символов.

import random
import time

from collections import Counter

def time_counter(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Время выполнения функции {func.__name__}: {end - start}')
        return result
    return wrapper

@time_counter
def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    return sorted(word1.lower()) == sorted(word2.lower())

@time_counter
def is_anagram_with_counter(word1, word2):
    if len(word1) != len(word2):
        return False
    return Counter(word1.lower()) == Counter(word2.lower())

# word = input("Enter a word: ")
# word_2 = input("Enter another word: ")
# print(f'Слова {word} и {word_2} это анаграммы: {is_anagram(word, word_2)}')

N = 100000
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

a = ''.join(random.choices(alphabet, k=N))

b_list = list(a)
random.shuffle(b_list)
b = ''.join(b_list)
print(f'Первая функция: {is_anagram(a, b)}')
print(f'Вторая: {is_anagram_with_counter(a, b)}')
