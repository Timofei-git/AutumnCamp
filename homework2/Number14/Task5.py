# Напиши функцию factorize(n), раскладывающую число на простые множители. Для 60 результат должен быть [2, 2, 3, 5], для 97 — [97].

def factorize(n):
    d = 2
    while n > 1:
        while n % d == 0:
            yield d
            n //= d
        d = d + 1

n = int(input("ВВедите число для разложения на множители: "))
for number in factorize(n):
    print(number, end=" ")