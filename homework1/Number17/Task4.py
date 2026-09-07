# Задача 4
# средний уровень
# Создай класс BankAccount с атрибутом balance и методами deposit(amount) и withdraw(amount).
# Метод withdraw не должен позволять уйти в минус — если денег не хватает, выводи сообщение об ошибке вместо списания.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __del__(self):
        print(f'Объект {self} удален')

    def withdraw(self, amount):
        if amount > self.balance:
            print('Not enough money!')
            return
        else:
            self.balance -= amount
            print(f'You withdrew ${amount}')

    def __str__(self):
        return f'Balance: {self.balance}'

    def deposit(self, amount):
        self.balance += amount

bank_account = BankAccount(100)
bank_account.deposit(50)
print(bank_account)
bank_account.withdraw(20)
print(bank_account)