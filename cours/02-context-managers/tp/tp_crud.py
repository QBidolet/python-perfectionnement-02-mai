import sqlite3
from contextlib import contextmanager


class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.cursor().close()
        self.conn.close()


def create_table(cursor):
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")


def insert_data(cursor, name, age):
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))


def read_data(cursor):
    cursor.execute("SELECT * FROM users;")
    return cursor.fetchall()


def update_data(cursor, user_id, new_name):
    cursor.execute("UPDATE users SET name = ? WHERE id = ?", (new_name, user_id))


def delete_data(cursor, user_id):
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))


@contextmanager
def database_connection(db_name):
    conn = sqlite3.connect(db_name)
    try:
        yield conn.cursor()
    finally:
        conn.commit()
        conn.cursor().close()
        conn.close()


with DatabaseConnection("ma_base.db") as cursor:
    create_table(cursor)
    insert_data(cursor, "Quentin BIDOLET", 50)
    print(read_data(cursor))
    update_data(cursor, 1, "DUPONT")
    print(read_data(cursor))
    delete_data(cursor, 1)
    print(read_data(cursor))

with database_connection("ma_base.db") as cursor:
    create_table(cursor)
    insert_data(cursor, "Quentin BIDOLET", 50)
    print(read_data(cursor))
    update_data(cursor, 1, "DUPONT")
    print(read_data(cursor))
    delete_data(cursor, 1)
    print(read_data(cursor))