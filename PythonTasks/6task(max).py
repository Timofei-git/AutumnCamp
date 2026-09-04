# Задача 6: Наибольшее из трёх
# Считайте три целых числа. Выведите наибольшее из них. Не используйте встроенную функцию max().

def findMax(nums):
    max = nums[0]
    for i in range(1,len(nums)):
        if nums[i] > max:
            max = nums[i]
    return max

list = []
listLength = int(input("Enter the length of the list: "))
for i in range(listLength):
    num = int(input(f"Enter the {i + 1} number: "))
    list.append(num)

print(f"The maximum number is {findMax(list)}")