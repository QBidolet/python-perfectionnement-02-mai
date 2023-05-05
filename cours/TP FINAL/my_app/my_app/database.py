import sqlite3
from contextlib import contextmanager
import threading

mutex = threading.Lock()


@contextmanager
def database_connection():
    with mutex:
        connection = sqlite3.connect("../app.db")
        cursor = connection.cursor()

        try:
            yield cursor
        finally:
            connection.commit()
            cursor.close()
            connection.close()


def create_table():
    with database_connection() as cursor:
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
        cursor.execute("CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, user_id INTEGER, text TEXT)")


if __name__ == '__main__':
    create_table()
