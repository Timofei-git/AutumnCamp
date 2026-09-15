# Напиши функцию simplify(numerator, denominator), сокращающую дробь до несократимого вида. Проверь на 12/18 и 100/250.
from math import gcd


def simplify(numerator, denominator):
    d = gcd(numerator, denominator)
    return numerator // d, denominator // d

print(simplify(12, 18))
