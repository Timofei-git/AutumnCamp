# Напиши функцию gcd(a, b) по алгоритму Евклида через цикл while. Проверь на парах (48, 18), (100, 75) и (17, 5).

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(48, 18))
print(gcd(100, 75))
print(gcd(17, 5))