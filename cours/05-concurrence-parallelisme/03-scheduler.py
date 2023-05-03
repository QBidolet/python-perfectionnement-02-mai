import threading
import time

travailler = True


def resolving_exercice():
    name = threading.current_thread().name
    count = 0
    while travailler:
        count += 1
    print(name, "a résolu", count, 'exercices\n')


if __name__ == "__main__":
    threading.Thread(target=resolving_exercice, name="Quentin").start()
    threading.Thread(target=resolving_exercice, name="Pierre").start()

    time.sleep(1)  # une seconde
    travailler = False  # Arrêter les deux threads
