# Задача 1
# базовый уровень
# Напиши декоратор, который перед выполнением обёрнутой функции печатает «Начинаю выполнение», а после неё — «Закончил выполнение».

def decor(func):
    def wrapper(*args,**kwargs):
        print(f"Начинаю выполнение функции {func.__name__}")
        result = func(*args,**kwargs)
        print(result)
        print(f'Заканчиваю выполнение функции')
        return result
    return wrapper

@decor
def count_sum(lst):
    return sum(lst)

count_sum([1, 2, 3, 4, 5, 6])