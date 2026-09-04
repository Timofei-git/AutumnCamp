#Задача 13: Количество цифр
#Считайте положительное целое число. Выведите, сколько в нём цифр: однозначное (1–9), двузначное (10–99), трёхзначное (100–999) или «больше трех знаков».

def define_the_amount_of_digits(number):
    if 10 > number >= 0:
        return 'The amount of digits is 1'
    elif 10 <= number < 100:
        return 'The amount of digits is 2'
    elif number >= 100 and number < 1000:
        return 'The amount of digits is 3'
    elif number >= 1000:
        return 'The amount of digits is 4 and more'
    else:
        return 'The number is negative'

number = int(input("Enter a number:"))
print(define_the_amount_of_digits(number))
