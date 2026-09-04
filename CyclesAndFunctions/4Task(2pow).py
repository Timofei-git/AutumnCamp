# Задача 4: Степень двойки
# Напишите функцию, которая проверяет, является ли число степенью двойки (2⁰=1, 2¹=2, 2²=4, и т.д.). Без циклов и встроенных функций вроде log.

def define_number_is_pow(number):
    if number == 1:
        return True

    if number < 1:
        return False

    return define_number_is_pow(number / 2)

print("The result is : ", define_number_is_pow(102))