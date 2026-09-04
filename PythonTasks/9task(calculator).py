#Задача 9: Калькулятор
#Считайте два числа и символ операции (+, -, *, /). Выполните соответствующую операцию и выведите результат.
# Обработайте деление на ноль и неизвестную операцию.

def calculator(num1, num2, symbol):
    if symbol == "+":
        return num1 + num2
    elif symbol == "-":
        return num1 - num2
    elif symbol == "*":
        return num1 * num2
    elif symbol == "/":
        if num2 == 0: return "You can not divide by zero"
        return round((num1 / num2), 2)
    else:
        return "Unrecognized operator"

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
symbol = input("Enter the operator: ")
print(calculator(num1, num2, symbol))