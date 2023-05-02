import contextlib


# 1. Définir le context le context manager
@contextlib.contextmanager
def simple_context_manager():
    print("Avant l'exécution du bloc")
    yield
    print("Après l'exécution du bloc")


with simple_context_manager():
    print("Dans le bloc.")

print("#" * 25)


# 2. Gérer les exceptions
@contextlib.contextmanager
def exception_context_manager():
    print("Avant l'exécution du bloc")
    try:
        yield
    except ValueError as e:
        print(f"Exception gérée : {e}")
    print("Après l'exécution du bloc")


with exception_context_manager():
    print("Dans le bloc")
    raise ValueError("Une erreur s'est produite.")

print("#" * 25)

# 3. Exemple classique : gestion d'une ressource
@contextlib.contextmanager
def ressource_context_manager(ressource_name):
    print(f"Ouverture de la ressource {ressource_name}")
    yield ressource_name
    print(f"Fermeture de la ressource {ressource_name}")


with ressource_context_manager("mon_fichier.txt") as ressource:
    print(f"Utilisation de la ressource {ressource}")
    ressource.write('test')
