# timeit est un module intégré qui fournit une manière simple de mesure le temps d'exécusion d'un code.

import timeit


def demo_function():
    return sum(range(1, 100))

# Mesurer le temps d'execution avec timeit.
time = timeit.timeit(demo_function, number=1000)
print(f"Temps d'exécution de demo_function pour 1000 appels: {time} secondes.")
