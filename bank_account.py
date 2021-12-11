class BankAccount:
    def __init__(self, bal):
        self.__balance = bal

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('Error: Insufficient balance.')

    def __str__(self):
        return 'The current balance is $' + format(self.__balance, ',.2f')
