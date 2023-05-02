# Création d'un context manager simple.

class SimpleRessource:
    def __enter__(self):
        print("Acquisition de la ressource.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Libération de la ressource.")


with SimpleRessource() as ressource:
    print("Utilisation de la ressource.")
# La ressource sera automatiquement libéré à la sortie du bloc.

print("#" * 25)


# pour gérer une exception
class RessourceWithException:
    def __enter__(self):
        print("Acquisition de la ressource.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print(f"Gestion de l'exception {exc_type}: {exc_value}")
        print("Libération de la ressource.")


with RessourceWithException() as ressource:
    print("Utilisation d'une ressource avec exception")
    # raise ValueError("Une erreur s'est produite.")

# Créer un context manager pour mesurer le temps d'exécution d'un bloc de code.
import time


class Timer:
    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, type, value, traceback):
        self.file_end = time.time() - self.start_time
        print(self.file_end)


with Timer():
    for _ in range(10000000):
        pass
