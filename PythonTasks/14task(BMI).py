#Задача 14: Расчет ИМТ
#Считайте рост (м) и вес (кг). Вычислите ИМТ = вес / рост².
#Выведите значение с 1 знаком и категорию: < 18.5 — «Недостаток веса», 18.5–24.9 — «Норма», 25–29.9 — «Избыточный вес», ≥ 30 — «Ожирение».

def define_the_bmi(weight, height):
    bmi = weight / (height**2)
    if bmi < 18.5:
        return f'BMI: {round(bmi, 2)}, the lack of weight'
    elif 18.5 < bmi < 25:
        return f'BMI: {round(bmi, 2)}, Normal weight'
    elif 25 <= bmi < 30:
        return f'BMI: {round(bmi, 2)}, High weight'
    else:
        return f'BMI: {round(bmi, 2)}, Obesity'

weight = int(input("Enter a weight:"))
height = int(input("Enter a height:"))
print(define_the_bmi(weight, height/100))