# Напиши функцию count_calls(n), которая считает, сколько рекурсивных вызовов делает наивный Фибоначчи для заданного n, и сравни это число с n для n = 10, 20 и 25.
calls = 0



def fib(n):
    global calls
    calls += 1

    if n == 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 1

    return fib(n-1) + fib(n-2)

def count_calls(n):
    global calls
    fib(n)
    return calls

nums = [10, 20, 25]
for n in nums:
    print(n,':', count_calls(n))

