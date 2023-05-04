import threading
from log_file import LogFile
from datetime import datetime


class ThreadSafeMeta(type):
    # def __new__(cls, name, bases, dct):
    #     print(f"création de la classe {name} avec la métaclasse ThreadSafeMeta")
    #     return super().__new__(cls, name, bases, dct)
    #
    # def __init__(cls, name, bases, dct):
    #     print(f"Initialisation de la classe {name} avec la ThreadSafeMeta")
    #     cls.mutex = threading.Lock()
    #     super().__init__(name, bases, dct)

    def __call__(cls, *args, **kwargs):
        # cls.mutex.acquire()
        # super().__call__(*args, **kwargs)
        # cls.mutex.release()
        print(f"Méthode call dans ThreadSafeMeta")
        obj = super().__call__(*args, **kwargs)
        obj.mutex = threading.Lock()
        return obj


class ThreadSafeLogger(LogFile, metaclass=ThreadSafeMeta):
    def write_log(self, log_level, message):
        with self.mutex:
            with self as file:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f'{timestamp} - {log_level} - {message}')


if __name__ == "__main__":
    logger = ThreadSafeLogger("logger.txt")
    logger.write_log("Information", "Message 1\n")
    logger.write_log("Error", "Message 2\n")
    logger.write_log("Warning", "Message 3\n")
