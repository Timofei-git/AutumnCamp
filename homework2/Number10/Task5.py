# Проверь стабильность своей сортировки: отсортируй список кортежей вида ("имя", отдел) по отделу и убедись, что имена внутри отдела сохранили исходный порядок.
# Затем поменяй в merge знак <= на < и посмотри, что изменится.

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][1] < right[j][1]:
            result.append(left[i])
            i += 1
        elif left[i][1] > right[j][1]:
            result.append(right[j])
            j += 1
        else:
            result.extend([left[i], right[j]])
            i += 1
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr


    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

employees = [("Аня", "IT"), ("Борис", "HR"), ("Вера", "IT")]

print(merge_sort(employees))