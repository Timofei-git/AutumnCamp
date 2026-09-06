# Задача 2
# базовый уровень
# Дана строка "Python,SQL,Docker,Git". Раздели её на список навыков и выведи, сколько всего навыков получилось.

string = "Python,SQL,Docker,Git"
new_list = string.split(',')
print(new_list)
print(len(new_list))