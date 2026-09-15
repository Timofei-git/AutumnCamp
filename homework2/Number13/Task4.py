# Дан список интервалов вида (начало, конец). Напиши функцию, выбирающую максимальное количество непересекающихся интервалов.

def find_intervals(intervals):
    intervals.sort(key = lambda x: x[1])

    result = []
    ends = intervals[0][1]
    result.append(list(intervals[0]))
    for start, end in intervals:
        if start > ends:
            result.append([start, end])
            ends = end

    return len(result)

print(find_intervals([(1, 4), (3, 5), (0, 6), (5, 7), (8, 9)]))


