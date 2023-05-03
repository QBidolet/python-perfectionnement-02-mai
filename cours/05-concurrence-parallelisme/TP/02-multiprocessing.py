import multiprocessing as mp


def sum_n(n):
    total = sum(range(1, n + 1))
    print(f"La somme des entiers des 1 à {n} est {total}")

if __name__ == "__main__":
    process_1 = mp.Process(target=sum_n, args=(5,))
    process_2 = mp.Process(target=sum_n, args=(15,))

    process_1.start()
    process_2.start()

    process_1.join()
    process_2.join()
