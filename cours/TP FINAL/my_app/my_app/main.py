from user import User
from message import Message
from crud import add_user, delete_user, get_user, add_message, get_message
from concurrency import add_message_concurrently

def main():
    # Exemple d'utilisation des opérations CRUD pour les users
    user = User(None, "Alice", 30)
    user = add_user(user)
    print(f"User ajouté : {user.id} {user.name} {user.age}")

    user_2 = User(None, "Bob", 52)
    user_2 = add_user(user_2)
    print(f"User ajouté : {user_2.id} {user_2.name} {user_2.age}")

    delete_user(user_2.id)
    user_2 = get_user(user_2.id)
    print(user_2)

    # Exemple de crud pour message
    message = Message(None, user.id, "Hello world!")
    message = add_message(message)
    print(f"Message ajouté {message.id} {message.text}")

    # Ajouter message en concurrence dans la base de données
    threads = []

    for i in range(1, 1_000):
        message = Message(None, user.id, f"Message {i}")
        thread = add_message_concurrently(message)
        threads.append(thread)

    for thread in threads:
        thread.join()

    message = get_message(3357)
    if message:
        print("Les messages ont bien été rentrés en base de données.")
    else:
        pass

if __name__ == '__main__':
    main()
