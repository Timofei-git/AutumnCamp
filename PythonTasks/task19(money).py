#Задача 19: Выдача сдачи
#Покупатель дает купюру номиналом 50, 100, 200, 500 или 1000 руб. за товар стоимостью price (целое, < номинала).
#Посчитайте сдачу и выразите её минимальным количеством купюр/монет: 100, 50, 10, 5, 2, 1 руб.

# def give_change(price, money):
#     change = money - price
#    if change < 0:
#    return "Change does not necessarily exceed the price"
#    return (f'100rub. - {change//100}, 50rub. - {change % 100 // 50}, 10rub. - {change % 100 % 50 // 10},'
#            f'5rub. - {change % 100 % 50 % 10 // 5}, 2rub. - {change % 100 % 50 % 10 % 5 // 2}, 1rub. - {change % 100 % 50 % 10 % 5 % 2}.')
#

def give_change(price, money):
    change = money - price
    if change < 0:
        return "Change does not necessarily exceed the price"

    changes_variety = [100, 50, 10, 5, 2, 1]
    str = ''
    for el in changes_variety:
        count = change // el
        change = change % el
        str = str + f"{el} - {count}, "
    return str

price = int(input('Enter price: '))
money = int(input('Enter money: '))
print(give_change(price, money))


