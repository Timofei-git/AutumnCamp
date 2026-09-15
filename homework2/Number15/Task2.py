# Дан список словарей с полями name и age. Отсортируй его сначала по возрасту, а при равном возрасте — по имени, одним вызовом sorted.

def sorted_lst(lst):

    return sorted(lst, key = lambda x: (x['age'], x['name']))

test_data = [
    {"name": "Влад", "age": 25},
    {"name": "Анна", "age": 25},
    {"name": "Диана", "age": 20},
    {"name": "Борис", "age": 25},
    {"name": "Глеб", "age": 20}
]
print(sorted_lst(test_data))