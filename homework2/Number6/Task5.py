# Напиши функцию longest_palindrome_word(text), которая находит самое длинное слово-палиндром в предложении. Проверь на предложении с несколькими палиндромами.

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

def longest_palindrome_word(text):
    words = text.split()
    longest = 0
    palindrome_word = []
    for word in words:
        word = word.strip(",!?.").lower()
        if len(word) > longest and is_palindrome(word):
            longest = len(word)
            palindrome_word.clear()
            palindrome_word.append(word)

        elif len(word) == longest and is_palindrome(word):
            palindrome_word.append(word)

    return palindrome_word

print(longest_palindrome_word("дед, топот, заказ, шалаш"))