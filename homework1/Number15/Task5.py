# Задача 5
# средний уровень
# Дана строка с email-адресом. Проверь, что в ней есть символ "@" и она заканчивается на ".ru" или ".com". Выведи «Похоже на email» или «Не похоже на email».

def email_checker(email):
    if '@' in email and (email.endswith('.com') or email.endswith('.ru')):
        return "Похоже на email"
    else:
        return 'Не похоже на email'

email_for_check = input('Введите email: ')
print(email_checker(email_for_check))