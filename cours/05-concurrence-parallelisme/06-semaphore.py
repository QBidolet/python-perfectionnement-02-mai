import threading
import random
import time

charger = threading.Semaphore(20)


def cellphone():
    name = threading.current_thread().name
    # Quand le téléphone charge, on écrit "is charging" et quand il a terminé on écrit "is done charging".
    with charger:
        print(name, "is charging")
        time.sleep(random.uniform(1, 2))
        # print(name, "is done charging")


if __name__ == "__main__":
    for number in range(100):
        threading.Thread(target=cellphone, name="Téléphone " + str(number)).start()
