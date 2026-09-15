# Напиши рекурсивную версию gcd и убедись, что она даёт те же ответы, что и итеративная.


def gcd(a, b):
    if not b:
        return a
    return gcd(b, a % b)

print(gcd(48, 18))
print(gcd(100, 75))
print(gcd(17, 5))