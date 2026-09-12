# Продемонстрируй стабильность встроенной сортировки: возьми список кортежей ("имя", отдел),
# отсортируй его сначала по имени, затем по отделу, и покажи, что внутри каждого отдела имена остались в алфавитном порядке.

departments_data = [
    ("Ярослав", "IT"),
    ("Анна", "HR"),
    ("Борис", "IT"),
    ("Ксения", "Sales"),
    ("Дарья", "IT"),
    ("Владимир", "Sales"),
    ("Глеб", "HR"),
    ("Ирина", "Sales"),
    ("Антон", "IT")
]

sorted_by_name = sorted(departments_data, key = lambda x: x[0])
print(f'Сортировка по имени: {sorted_by_name}')
sorted_by_department = sorted(sorted_by_name, key = lambda x: x[1])
print(f'Сортировка по отделу: {sorted_by_department}')
