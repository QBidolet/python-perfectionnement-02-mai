import threading
import time

bank_count = 500

semaphore = threading.Semaphore(1)

def shop(nombre_transaction):
    global bank_count
    for i in range(nombre_transaction):
        with semaphore:
            bank_count -= 100 # 1ms


def salary(nombre_transaction):
    global bank_count
    for i in range(nombre_transaction):
        with semaphore:
            bank_count += 100 # 1ms


if __name__ == '__main__':
    nombre_transaction = 10_000_000
    achat = threading.Thread(target=shop, args=(nombre_transaction,))
    salaire = threading.Thread(target=salary, args=(nombre_transaction,))
    achat.start()
    salaire.start()
    # la fct join fait qu'on passe pas à la suite tant que les thread sont pas finis (donc qu'ils ont acheté 10000000)
    achat.join()
    salaire.join()
    print("Nous avons  " + str(bank_count) + "euros.")
