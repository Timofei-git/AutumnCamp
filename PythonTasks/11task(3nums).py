#Задача 11: Проверка диапазона
#Считайте три числа: a, b и x. Определите, попадает ли x в закрытый отрезок [a, b].
#Выведите «Внутри» или «Снаружи». Гарантируется, что a ≤ b.

def ifTheNumberInRange(num,low,high):
    if low <= high:
        if num >= low and num <= high:
            return f"Number {num} is between {low} and {high}"
        else:
            return f"Number {num} is not between {low} and {high}"
    else:
        return f"The low number {low} is bigger than the high number {high}"

low = int(input("Enter low number:"))
high = int(input("Enter high number:"))
x = int(input("Enter your choice:"))
print(ifTheNumberInRange(x,low,high))