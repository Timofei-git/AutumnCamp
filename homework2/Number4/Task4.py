# Напиши рекурсивную функцию reverse_string(s), которая разворачивает строку задом наперёд. Не используй срезы вида [::-1].

def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

print(reverse_string("abc"))
