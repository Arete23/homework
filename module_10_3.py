from threading import Thread, Lock
from random import randint
from time import sleep

class Bank(Thread):

    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = Lock()


    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            y = randint(50, 500)
            self.balance += y
            print(f'Пополнение: {y}. Баланс: {self.balance}')
            sleep(0.001)


    def take(self):
        for i in range(100):
            x = randint(50,500)
            print(f'Запрос на {x}')
            if self.balance >= x:
                self.balance -= x
                print(f'Снятие: {x}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')
