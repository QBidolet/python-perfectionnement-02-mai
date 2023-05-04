import threading


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        new_balance = self.balance + amount
        self.balance = new_balance

    def withdraw(self, amount):
        new_balance = self.balance - amount
        self.balance = new_balance


def deposit_money(account, amount, times):
    for _ in range(times):
        account.deposit(amount)

def withdraw_money(account, amount, times):
    for _ in range(times):
        account.withdraw(amount)


if __name__ == '__main__':
    num_transaction = 1_000_000
    account = BankAccount(1000)

    deposit_thread = threading.Thread(target=deposit_money, args=(account, 10, num_transaction))
    withdraw_thread = threading.Thread(target=withdraw_money, args=(account, 10, num_transaction))

    deposit_thread.start()
    withdraw_thread.start()

    deposit_thread.join()
    deposit_thread.join()

    print(f"Résultat final : {account.balance}")
