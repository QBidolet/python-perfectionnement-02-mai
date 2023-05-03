import threading

book_count = 0
mutex = threading.Lock()

def shopper():
    global book_count
    for i in range(10_000_000):
        mutex.acquire()
        book_count += 1
        mutex.release()

if __name__ == '__main__':
    quentin = threading.Thread(target=shopper)
    pierre = threading.Thread(target=shopper)
    quentin.start()
    pierre.start()

    quentin.join()
    pierre.join()
    print("Nous avons achetés " + str(book_count) + " livres.")
