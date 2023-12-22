#  Напишите программу, которая будет симулировать банк с использованием потоков и объектов типа Lock. Реализуйте методы deposit и
# withdraw, которые будут добавлять и снимать деньги со счета клиента
# соответственно. Гарантируйте, что доступ к счету будет синхронизирован с помощью объекта типа Lock.
import threading


class Account:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.account_lock = threading.Lock()

    def deposit(self, deposit_amount):
        with self.account_lock:
            old_balance = self.balance
            self.balance = old_balance + deposit_amount
            print(f"Deposited {deposit_amount}. New balance: {self.balance}")

    def withdraw(self, withdrawal_amount):
        with self.account_lock:
            if withdrawal_amount <= self.balance:
                self.balance -= withdrawal_amount
                print(f"Withdrew {withdrawal_amount}. New balance: {self.balance}")
            else:
                print("Insufficient funds.")


def bank_activity_simulation(customer_account):
    for _ in range(5):
        customer_account.deposit(10000)
        customer_account.withdraw(50)


if __name__ == "__main__":
    customer_account = Account()

    bank_threads = []
    for _ in range(3):
        activity_thread = threading.Thread(target=bank_activity_simulation, args=(customer_account,))
        bank_threads.append(activity_thread)
        activity_thread.start()

    for activity_thread in bank_threads:
        activity_thread.join()

    print("Final balance:", customer_account.balance)
