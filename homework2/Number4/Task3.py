# Напиши рекурсивную функцию countdown(n), которая печатает числа от n до 1, каждое с новой строки.

def countdown(n):
    if n == 1:
        return "1"
    return f"{n},\n{countdown(n-1)}\n"

print(countdown(5))