import threading


def sum_n(n):
    total = sum(range(1, n + 1))
    print(f"La somme des entiers des 1 à {n} est {total}")


thread_1 = threading.Thread(target=sum_n, args=(5,))
thread_2 = threading.Thread(target=sum_n, args=(15,))

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()
