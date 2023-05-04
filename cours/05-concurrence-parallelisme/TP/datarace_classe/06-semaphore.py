import threading


class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.semaphore = threading.Semaphore(1)

    def deposit(self, amount):
        with self.semaphore:
            new_balance = self.balance + amount
            self.balance = new_balance

    def withdraw(self, amount):
        with self.semaphore:
            new_balance = self.balance - amount
            self.balance = new_balance


def deposit_money(account, amount, times):
    for _ in range(times):
        account.deposit(amount)


def withdraw_money(account, amount, times):
    for _ in range(times):
        account.withdraw(amount)


if __name__ == '__main__':
    account = BankAccount(1000)
    num_transactions = 1_000_000

    deposit_thread = threading.Thread(target=deposit_money, args=(account, 10, num_transactions))
    withdraw_thread = threading.Thread(target=withdraw_money, args=(account, 10, num_transactions))

    deposit_thread.start()
    withdraw_thread.start()

    deposit_thread.join()
    withdraw_thread.join()

    print(f"Final balance: {account.balance}")
