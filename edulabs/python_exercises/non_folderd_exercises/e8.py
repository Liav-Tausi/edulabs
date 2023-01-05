import datetime
import threading


class ThreadSafeBankAccount:

    def __init__(self, account_number: int, name: str):
        self.name: str = name
        self.account_number: int = account_number
        self.balance: int = 0
        self.list_of_transactions: list = list()

        self.lock1: 'threading' = threading.Lock()
        self.lock2: 'threading' = threading.Lock()


    def deposit(self, amount: int) -> None:
        date = datetime.datetime.utcnow().date()
        if amount > 0:
            with self.lock1:
                amount += self.balance
                self.list_of_transactions.extend(('deposit', date))

    def withdraw(self, amount: int) -> None:
        date = datetime.datetime.utcnow().date()
        if 0 < amount <= self.balance:
            with self.lock2:
                amount -= self.balance
                self.list_of_transactions.extend(('withdraw', date))


if __name__ == '__main__':
    try:
        my_account = ThreadSafeBankAccount(123456, "Israel Israeli")


        def multiple_transactions_deposit(account):
            for i in range(100, 2000000, 10):
                account.deposit(i)

        def multiple_transactions_withdraw(account):
            for i in range(100, 2000000, 10):
                account.withdraw(i)

        t1 = threading.Thread(target=multiple_transactions_deposit, args=(my_account,))
        t2 = threading.Thread(target=multiple_transactions_deposit, args=(my_account,))
        t3 = threading.Thread(target=multiple_transactions_withdraw, args=(my_account,))
        t4 = threading.Thread(target=multiple_transactions_withdraw, args=(my_account,))

        t1.start()
        t2.start()
        t3.start()
        t4.start()

        t1.join()
        t2.join()
        t3.join()
        t4.join()

        assert my_account.balance == 0, \
            f"Expected balance: 0, received: {my_account.balance}"
        assert len(my_account.list_of_transactions) == 799960, \
            f"Expected transactions: 799960, received: len(my_account.transactions_list)"
    except Exception:
        print('Error')
