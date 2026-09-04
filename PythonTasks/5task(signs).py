#Задача 5: Знак числа
# Считайте вещественное число. Определите его знак: выведите «Положительное», «Отрицательное» или «Ноль».

number = float(input('Enter a number: '))

if number == 0:
    print('You entered 0')
elif number > 0:
    print('You entered positive number')
else:
    print('You entered negative number')