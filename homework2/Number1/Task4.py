# Возьми список из 1000 случайных чисел. Замерь время работы своей функции суммы и своей функции всех пар. Выведи обе цифры и объясни разницу.

import random, Task2, Task3
import time

lst = [random.randint(1,10000) for i in range(1000)]
start = time.time()
print(Task2.count_sum(lst))
all_time = time.time() - start
start = time.time()
print(Task3.find_pairs(lst))
all_time_2 = time.time() - start
print(f'Время выполнения суммы: {all_time}, время выполнения поиска пар: {all_time_2}')
# время нахождения суммы всегда будет меньше из-за сложности O(n), у алгоритма поиска пар сложность - O(n**2)