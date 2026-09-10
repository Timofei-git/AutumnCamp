# Напиши функцию is_palindrome(text), проверяющую слово на палиндром двумя указателями. Не используй срез [::-1].
# Доработай функцию так, чтобы она игнорировала пробелы и регистр букв. Проверь на фразе «А роза упала на лапу Азора»

def is_palindrome(text):
    new_text = ('').join( c.lower() for c in text if c.isalnum())
    left = 0
    right = len(new_text)-1
    while left < right:
        if new_text[left] != new_text[right]:
            return False
        left += 1
        right -= 1
    return True

word_for_check = input("Enter a word: ")
print(f'Слово {word_for_check} палиндром: {is_palindrome(word_for_check)}')
print(f'Слово {"А роза упала на лапу Азора"} палиндром: {is_palindrome("А роза упала на лапу Азора")}')