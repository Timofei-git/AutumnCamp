# Задача 5
# средний уровень
# Напиши программу с тремя переменными: начальный баланс счёта, сумма пополнения и сумма списания.
# Выведи баланс после пополнения, а затем — после списания, показав оба промежуточных состояния.

current_balance = 1000
income = 500
outcome = 200
print(f'Balance after income: {current_balance + income}')
print(f'Balance after outcome: {current_balance + income - outcome}')
