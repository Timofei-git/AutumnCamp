#Задача 4: Четность числа
# Считайте целое число. Выведите «Чётное», если число делится на 2, иначе — «Нечётное».
number = int(input('Enter number: '))

if number == 0:
    print('You entered 0')
elif number % 2 == 0:
    print('You entered a even')
else:
    print('You entered a odd')
