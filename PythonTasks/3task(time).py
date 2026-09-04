#Задача 3: Часы и минуты
# Дано количество минут (целое число). Выведите, сколько это полных часов и остаток минут.

def countTime(minutes):
    return minutes // 60, minutes % 60

min = int(input('Enter minutes: '))
hours, minutes = countTime(min)
print(f"The time is {hours} hours and {minutes} minutes")