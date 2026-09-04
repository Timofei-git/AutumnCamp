#Задача 20: Цифровой корень
#Цифровой корень числа — сумма его цифр, применяемая повторно до получения однозначного числа.
# Считайте натуральное число и выведите его цифровой корень, не используя рекурсию и циклы — только арифметику и условные операторы.

def finding_square(number):
    if number < 10 and number >= 0:
        return number
    elif number % 9  == 0:
            return 9
    else:
        return number % 9

    # while number >= 10:
    #     sum = 0
    #     while number > 0:
    #         sum += number % 10
    #         number //= 10
    #
    #     number = sum

    #return number

number = int(input("Enter a number: "))
print(finding_square(number))
