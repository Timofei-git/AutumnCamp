# 1 Напиши функцию make_change(amount), которая жадно выдаёт сдачу монетами 1, 5, 10, 25 и возвращает список монет. Проверь на суммах 63, 99 и 7.

# я сразу писал ввиде словаря
# 2 Перепиши make_change так, чтобы она возвращала словарь «номинал: количество» и использовала целочисленное деление вместо цикла while.

def make_change(amount,coins):
    if amount < 0:
        return -1


    result = {}
    for coin in coins:
        result[coin] = amount // coin
        amount = amount % coin

    return result


print(make_change(63, [25, 10, 5, 1]))

