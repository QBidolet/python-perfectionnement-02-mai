nombres = [1, 2, 3, 4]

# python crée en interne un Iterateur et le manipule pour parcourir la liste.
# for nombre in nombres:
#     print(nombre)

# iter()
iterateur = iter(nombres)
# print(next(iterateur))
# print(next(iterateur))
# print(next(iterateur))
# print(next(iterateur))
# print(next(iterateur))


# Création d'un Iterateur personnalisé
class MonIterateur:
    def __init__(self, debut, fin):
        self.debut = debut
        self.fin = fin

    def __iter__(self):
        return self

    def __next__(self):
        if self.debut >= self.fin:
            raise StopIteration
        self.debut += 1
        return self.debut - 1


# Utilisation
mon_iterateur = MonIterateur(1, 6)

# print(mon_iterateur.__iter__)
for nombre in mon_iterateur:
    print(nombre)