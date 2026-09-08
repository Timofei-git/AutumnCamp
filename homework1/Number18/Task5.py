# Задача 5
# средний уровень
# Напиши декоратор с параметром @repeat(n), который заставляет обёрнутую функцию выполниться n раз подряд при каждом вызове.

def repeat(n):
    def decor(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decor

@repeat(3)
def say_hello():
    print("hello")

say_hello()