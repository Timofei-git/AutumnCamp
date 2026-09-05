# Задача 5
# средний уровень
# Напиши функцию, которая принимает строку и возвращает словарь, где ключи — буквы этой строки, а значения — сколько раз каждая буква встретилась (без учёта регистра).

def make_dictionary(string):
    final_dictionary = {}
    for letter in string.lower():
        if letter not in final_dictionary:
            final_dictionary[letter] = 1
        elif letter in final_dictionary:
            final_dictionary[letter] += 1

    return final_dictionary

print(make_dictionary('My name is Tima'))