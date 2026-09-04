#Задача 8: Високосный год
#Считайте год. Год является високосным, если делится на 4, но не делится на 100, или делится на 400. Выведите «Високосный» или «Обычный».

year = int(input("Enter the year: "))

if year % 4 == 0 and year % 100 !=0 or year % 400 == 0:
    print("The year is leap")
else:
    print("The year is not leap")
