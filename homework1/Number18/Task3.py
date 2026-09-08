# Задача 3
# базовый уровень
# Напиши декоратор, который считает и печатает, сколько раз была вызвана обёрнутая функция.

def decor(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print("Функция началась: ")
        result = func(*args, **kwargs)
        print("Функция закончила выполняться")
        return result
    wrapper.calls = 0
    return wrapper

@decor
def say_hello():
    print("Привет")

say_hello()
say_hello()
print(f'Функция say_hello вызвана {say_hello.calls}')


