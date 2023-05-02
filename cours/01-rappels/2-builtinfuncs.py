# Présentation rapide des fonctions intégrés.

list_1 = [1, 2, 3, 4, 5]

# any renvoie True si au moins une des valeurs vaut True.
print(any(list_1))

# all renvoie True si toutes la valeurs valent True.
print(all(list_1))

# min et max : retourne le minimum et le maximum dans une séquence
print(min(list_1))
print(max(list_1))

# sum fait la somme
print(sum(list_1))

# Itérateurs

days = ["Sun", "Mon", "Tue", "Web", "Thu", "Fri", "Sat"]
days_fr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

i = iter(days)
print(next(i))
print(i)
print(next(i))
print(next(i))

# fonctions génératrices
def compteur(n):
    for i in range(n):
        # yield suivi de la valeur à renvoyer à chaque itération
        yield i

i = compteur(10)
print(next(i))
print(next(i))
print(next(i))
for i in compteur(10):
    print(i)

for i in range(len(days)):
    print(i + 1, days[i])
