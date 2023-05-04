# cprofile fournit des statistiques détaillées sur le temps d'exécution et le nombre d'appels.
# C'est ce qu'on appelle un outil de profillage.

import cProfile


def demo_function():
    return sum(range(1, 1_000_000))


# Profilage du code
profiler = cProfile.Profile()
profiler.enable()
for i in range(1, 100):
    demo_function()

profiler.disable()
profiler.print_stats()
