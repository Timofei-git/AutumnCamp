#Задача 18: Перевод в другую систему
#Считайте неотрицательное целое число и основание системы счисления (2, 8 или 16).
#Выведите число в этой системе. Не используйте встроенные bin(), oct(), hex().

ERROR = -1
bases = [2, 8, 16]
def check_num(number, base):
    if number < 0 or base < 0:
        return False
    if base in bases:
        return True
    return False

def tranfer_to_second(number):
    res = ''
    while number > 0:
        res = str(number % 2)+ res
        number //= 2
    return res

def transfer_to_eights(number):
    res = ''
    while number > 0:
        res = str(number % 8) + res
        number //= 8
    return res

hex_dig = {10:"A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
def transfer_to_sixteens(number):
    res = ''
    while number > 0:
        if number % 16 < 10:
            res = str(number % 16) + res
        else:
            res = hex_dig[number%16] + res
        number //= 16
    return res

def define_which_to_use(base, number):

    if check_num(number, base):
        if number == 0: return 0
        if base == 2:
            return tranfer_to_second(number)
        elif base == 8:
            return transfer_to_eights(number)
        else:
            return transfer_to_sixteens(number)
    else:
        return ERROR

number = int(input("Enter a number:"))
base = int(input("Enter a base:"))
print(define_which_to_use(base, number))