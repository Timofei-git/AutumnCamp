# Задача 2
# базовый уровень
# Добавь в наивную версию глобальный счётчик вызовов функции и выведи, сколько раз она вызвалась при вычислении fib(20).

GLOBAL_COUNTER = 0

def fib(n):
    global GLOBAL_COUNTER
    GLOBAL_COUNTER += 1
    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)

print(f'Функция func(25), результат: {fib(10)} выполнилась {GLOBAL_COUNTER} раз')