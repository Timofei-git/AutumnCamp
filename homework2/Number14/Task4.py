# Напиши функцию primes_up_to(n), возвращающую список всех простых чисел от 2 до n включительно, используя свою is_prime.
def is_prime(n):
    if n < 2:
        return False

    if n == 2:
        return True

    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1

    return True

def primes_up_to(n):
    for i in range(3, n):
        if is_prime(i):
            yield i

n = int(input(f'Введите число до которого хотите выполнить проверку: '))
for i in primes_up_to(n):
    print(i)