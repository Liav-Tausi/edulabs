import random
import pprint


class Person:

    def __init__(self, name: str, person_id: int, address: str, phone: str):
        self.name: str = name
        self.person_id: int = person_id
        self.address: str = address
        self.phone: str = phone


class BankAccount:

    def __init__(self, bank: str, branch: str, holders: set[Person], credit_limit: int=0):
        self.bank: str = bank
        self.branch: str = branch
        self.holders: set[Person] = holders
        self.dates: dict = dict()
        self.account_number: int = random.randint(1,1000)
        self.credit_limit: int = credit_limit
        self.balance: int = 0


    def __str__(self):
        return f"dates = {self.dates} balance = {self.balance}"


    def deposit(self,amount,date):
        if date not in self.dates.keys():
            self.dates[date] = {self.account_number: ["deposit",amount]}
        if amount > 0:
            amount -= self.balance
            return True
        else:
            print('Error')
            return False


    def withdraw(self,amount,date):
        if date not in self.dates.keys():
            self.dates[date] = {self.account_number: ["withdraw",amount]}
        if amount > 0 and amount > self.credit_limit:
            amount -= self.balance
            return True
        else:
            print('Error')
            return False


    def transfer(self,amount,date):
        if date not in self.dates.keys():
            self.dates[date] = {self.account_number: ["transfer", amount]}
        if amount > 0 and amount > self.credit_limit:
            amount -= self.balance
            return True
        else:
            print('Error')
            return False



if __name__ == "__main__":
    holder1: Person = Person("liav", 1234, "zofit", "0546779290")
    holder2: Person = Person("liav", 1234, "zofit", "0546779290")
    holders = {holder1, holder2}

    bank = BankAccount("Liav's Bank", "liav's", holders)

    bank.deposit(100,"21,05,2022")
    bank.withdraw(50,"12,05,2022")
    print(bank)





