# Задача 7: Второй максимум
# Найдите второе по величине число в списке. Гарантируется, что в списке минимум 2 различных элемента.

def entering(count):
    numbers = []
    for i in range(count):
        num = int(input(f"Enter {i + 1} number: "))
        numbers.append(num)
    return numbers

def finding_second_largest(numbers):
    temp = numbers.copy()
    temp.remove(max(temp))
    return max(temp)

amount = int(input("Enter the amount of list: "))
numbers = entering(amount)
print(f'The second largest number is {finding_second_largest(numbers)}')

