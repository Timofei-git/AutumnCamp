#Задача 1: Сумма в диапазоне
#Напишите функцию, которая вычисляет сумму всех чисел от start до end включительно, используя цикл. Не используйте встроенную функцию sum().

def sum_numbers(start, end):
    # sum = 0
    # for i in range(start, end + 1):
    #     sum += i
    # return sum
    return (start + end) // 2 * (end - start + 1)

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
print(sum_numbers(first, second))