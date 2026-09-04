#   Задача 7: Деление с обработкой
# Считайте два числа a и b. Если b равно нулю — выведите «Деление на ноль невозможно», иначе выведите результат деления a на b с двумя знаками после запятой.

dividend = int(input("Enter the dividend: "))
divisor = int(input("Enter the divisor: "))

if divisor == 0:
    print("You can't divide by zero")
else:
    print(round((dividend / divisor), 2))