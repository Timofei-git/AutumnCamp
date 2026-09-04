#Задача 10: Оценка по баллам
#Считайте балл от 0 до 100. Выведите оценку: 90–100 → «A», 80–89 → «B», 70–79 → «C», 60–69 → «D», 0–59 → «F».
# Если балл вне диапазона — выведите «Ошибка».

def defineMark(mark):
    if mark > 100 or mark < 0:
        return "Mark can't be so high"
    elif mark > 89:
        return "A"
    elif mark > 79:
        return "B"
    elif mark > 69:
        return "C"
    elif mark > 59:
        return "D"
    else:
        return "F"

mark = int(input("Enter mark:"))
print(f'Your grade is {defineMark(mark)}')

