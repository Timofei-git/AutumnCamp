# Задача 5 (сложный) — Анаграммы в тексте
#
# Дан текст и слово-образец. Найди все подстроки текста той же длины, что и образец, которые являются анаграммами этого образца (без учёта регистра).

def make_dictionary(string):
    final_dictionary = {}
    for letter in string:
        if letter not in final_dictionary:
            final_dictionary[letter] = 1
        else:
            final_dictionary[letter] += 1
    return final_dictionary

def find_word_anagram(text, founded_word):
    anagram = []
    dictionary_from_founded_word = make_dictionary(founded_word.lower())
    for word in text.split():
        if len(word) != len(founded_word):
            continue
        if make_dictionary(word.lower()) == dictionary_from_founded_word:
            anagram.append(word)
    return anagram

text = "силан налис слина банан налис"
word = "слина"
print(find_word_anagram(text, word))