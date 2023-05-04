from thread_safe_logger import ThreadSafeLogger
import threading


def worker(logger, log_level, message):
    logger.write_log(log_level, message)


if __name__ == "__main__":
    logger = ThreadSafeLogger("logfile.txt")

    threads = []

    for i in range(5000):
        thread = threading.Thread(target=worker, args=(logger, "Informations", f"Je suis le thread {i}.\n"))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
