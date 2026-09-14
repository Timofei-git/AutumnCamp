# Задача 5
# средний уровень
# Напиши функцию, которая находит максимальную глубину рекурсии, при которой Python ещё не падает с RecursionError.
# Оберни вызов в try/except и выводи достигнутое значение.

def find_max_depth(counter= 0):


    try:

        return find_max_depth(counter + 1)
    except RecursionError:
        print('Достигнут максимум')
        return counter

print(find_max_depth())
