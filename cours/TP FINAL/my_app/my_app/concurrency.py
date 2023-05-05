import threading
from crud import add_message


def add_message_concurrently(message):
    thread = threading.Thread(target=add_message, args=(message,))
    thread.start()
    return thread
