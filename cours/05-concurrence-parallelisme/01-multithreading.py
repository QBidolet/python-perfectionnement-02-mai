import threading
import os


def cpu_waster():
    while True:
        pass


if __name__ == "__main__":
    # Afficher les informations du processus
    print('ID du processus : ' + str(os.getpid()))
    print("Thread count : " + str(threading.activeCount()))

    for thread in threading.enumerate():
        print(thread)

    print("#" * 25)
    for i in range(4):
        threading.Thread(target=cpu_waster).start()

    # Afficher des informations à propos des Thread
    print("Thread count " + str(threading.activeCount()))
    for thread in threading.enumerate():
        print(thread)
