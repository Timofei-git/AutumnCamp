# Отсортируй список слов ["python", "go", "javascript", "c"] по длине, а затем по алфавиту. Используй встроенную сортировку с параметром key.

lst = ["python", "go", "javascript", "c"]

sorted_lst = sorted(lst, key = lambda x: (len(x)))
print(sorted_lst)
sorted_lst = sorted(lst, key = lambda x: x[0])
print(sorted_lst)