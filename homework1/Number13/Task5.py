# Задача 5
# средний уровень
# Даны два списка одинаковой длины: имена студентов и их оценки.
# Собери из них словарь имя → оценка с помощью zip и dict, а затем выведи имена всех студентов с оценкой выше 4.

student_names = ["Tima", "Anton", "Vlad", "Artem"]
lessons = ["Math", "English", "Physics", "Science"]
student_marks = [[3, 2, 5, 6], [2, 7, 8, 9], [2, None, 2, None], [10, 4, 5, 7]]

students_marks = dict(zip(student_names, student_marks))

student_subject_marks = {
    name: dict(zip(lessons, marks))
    for name, marks in students_marks.items()
}

print(student_subject_marks)