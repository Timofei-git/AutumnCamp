# Задача 8: Пересечение массивов
# Найдите все элементы, которые есть в обоих массивах (пересечение). Результат должен содержать уникальные элементы.

def create_list(number):
    numbers = []
    if number <= 0:
        return []
    else:
        for i in range(number):
            num = int(input(f"Enter {i + 1} number: "))
            numbers.append(num)

    return numbers

def find_intersection(list1, list2):
    return list(set(list1) & set(list2)) #Пересечение


def find_unic(list1, list2):
    return list(set(list1) ^ set(list2)) #Симм разность

def final_function():
    amount = int(input("Enter the size of 1 list: "))
    first_list = create_list(amount)
    amount2 = int(input("Enter the size of 2 list: "))
    second_list = create_list(amount2)
    return find_intersection(first_list, second_list), find_unic(first_list, second_list)

intersection, unic = final_function()
print(f'Intersection numbers are: {intersection}, unic numbers are: {unic}')

