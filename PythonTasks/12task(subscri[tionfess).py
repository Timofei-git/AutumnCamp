#Задача 12: Расчет абонентской платы
#Абонент платит 300 руб/мес за 100 минут. Каждая дополнительная минута стоит 3 руб.
#Считайте количество минут, выведите итоговую стоимость.

def defineSubscriptionFee(minutes):
    if minutes <= 100:
        return f'Your subscription fee is 300'
    else:
        return f'Your subscription fee is {300 + (minutes - 100) * 3}'

minutes = int(input("Enter minutes:"))
print(defineSubscriptionFee(minutes))