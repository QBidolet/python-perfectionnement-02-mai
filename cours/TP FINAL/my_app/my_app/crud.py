from database import database_connection
from user import User
from message import Message

# CRUD user
def add_user(user):
    with database_connection() as cursor:
        cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (user.name, user.age))
        # Amélioration : Renvoyer l'objet user avec l'id de complété.
        user.id = cursor.lastrowid
    return user


def get_user(user_id):
    with database_connection() as cursor:
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        user = cursor.fetchone()
    if user is not None:
        return User(user.id, user.name, user.age)


def update_user(user):
    with database_connection() as cursor:
        cursor.execute("UPDATE users SET name = ?, age = ? WHERE id = ?", (user.name, user.age, user.id))


def delete_user(user_id):
    with database_connection() as cursor:
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))


# CRUD message
def add_message(message):
    with database_connection() as cursor:
        cursor.execute("INSERT INTO messages (user_id, text) VALUES (?, ?)", (message.user_id, message.text))
        # Amélioration : Renvoyer l'objet message avec l'id de complété.
        message.id = cursor.lastrowid
    if message is not None:
        return message


def get_message(message_id):
    with database_connection() as cursor:
        cursor.execute("SELECT * FROM messages WHERE id = ?", (message_id,))
        message = cursor.fetchone()
    if message is not None:
        return Message(*message)


def update_message(message):
    with database_connection() as cursor:
        cursor.execute("UPDATE messages SET text = ? WHERE id = ?", (message.text, message.id))


def delete_message(message_id):
    with database_connection() as cursor:
        cursor.execute("DELETE FROM messages WHERE id = ?", (message_id,))
