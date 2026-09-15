# Напиши функцию is_rotation(s1, s2), проверяющую, является ли вторая строка вращением первой. Проверь на "waterbottle" и "erbottlewat".

def is_rotation(s1, s2):
    return len(s1) == len(s2) and s1 == s2[::-1]

print(is_rotation("waterbottle", "erbottlewat"))
reversed = "waterbottle"[::-1]
print(is_rotation(reversed, "waterbottle"))