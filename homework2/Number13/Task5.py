# Дан список весов предметов и вместимость рюкзака. Напиши жадное решение, которое кладёт предметы по возрастанию веса, пока они помещаются, и возвращает их количество.
# В комментарии укажи, для какой задачи такая жадность оптимальна, а для какой — нет.

def find_optimal_objects(amount, objects):
    if amount <= 0:
        return 0
    objects.sort(key=lambda x: x[1])
    result = {}
    for name, weight in objects:
        if amount < weight:
            break

        result[name] = weight
        amount -= weight

    return len(result)

amount = 10
items = [("Книга", 3), ("Смартфон", 1), ("Ноутбук", 5),("Ручка", 2), ("Гантель", 3)]

print(find_optimal_objects(amount, items))