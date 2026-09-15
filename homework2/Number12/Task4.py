# Напиши функцию longest_unique(s), которая находит длину самой длинной подстроки без повторяющихся символов. Используй окно переменной ширины.



def longest_unique(s):
    new_str = []
    right = 0
    left = 0
    max_len = 0
    while right != len(s):
        if s[right] not in new_str:
            new_str.append(s[right])
            right += 1
            max_len = max(max_len, right - left)
        else:
            while s[left] != s[right]:
                new_str.remove(s[left])
                left += 1

            new_str.remove(s[left])
            left += 1


    return max_len

print(longest_unique("abcabcdebab"))


