#Задача 17: Проверка даты
#Считайте день, месяц и год. Проверьте корректность даты: месяц 1–12, день 1–(кол-во дней в месяце),
# учитывая високосный год для февраля. Выведите «Корректная» или «Некорректная».

INCORRECT_DATE = 'Incorrect date'
def define_if_year_is_leap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

big_month = (1, 3, 5, 7, 8, 10, 12)
small_month = (4, 6, 9, 11)
def define_the_date(day, month, year):
   is_leap_year = define_if_year_is_leap(year)
   if month > 12 or month < 1:
       return INCORRECT_DATE
   elif month in big_month:
       if day > 31 or day < 1:
           return INCORRECT_DATE
       else:
           return f'The date is {day}.{month}.{year}'
   elif month in small_month:
       if day > 30 or day < 1:
           return INCORRECT_DATE
       else:
           return f'The date is {day}.{month}.{year}'
   else:
       if is_leap_year:
           if day > 29 or day < 1:
               return INCORRECT_DATE
           else:
               return f'The date is {day}.{month}.{year}'
       elif day > 28 or day < 1:
           return INCORRECT_DATE
       else:
           return f'The date is {day}.{month}.{year}'

day = int(input("Enter a day:"))
month = int(input("Enter a month:"))
year = int(input("Enter a year:"))
print(define_the_date(day, month, year))



