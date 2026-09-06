# Задача 3
# базовый уровень
# Дан список слов. С помощью генератора списка получи список их длин.

def find_length(lst):
    return [len(word.strip()) for word in lst]

words = ["яблоко", "мир", "программирование", "кот", "солнце", "дом"]
print(find_length(words))