# Utilisation basique de try ... finally

a = 2

try:
    # code potentiellement sujet à des erreurs
    x = 1 / a
except ZeroDivisionError:
    print("Division par zéro !")
finally:
    # Ce bloc de code sera toujours exécuté
    print("Exemple 1 terminé")

# try ... finally sans gestion d'erreur
try:
    x = 1 / a
finally:
    print("Exemple 2 terminé")


# pour gérer les ressources
def exemple_3():
    f = open("exemple.txt", "w")
    try:
        f.write("Hello World !")
    finally:
        print("Exemple 3 terminé.")
        f.close()


exemple_3()

# Exemple 4 : avec plusieurs exceptions
try:
    x = int("abc")
    y = 1 / 0
except ZeroDivisionError:
    print("Division par zéro !")
except ValueError:
    print("Value Error")

print("#"*25)
# utilisation dans une boucle
for i in range(5):
    try:
        if i % 2 == 0:
            print("Nombre pair")
        else:
            x = 1 / 0
    except ZeroDivisionError:
        print("Erreur")
    else:
        print("else")
    finally:
        print("Itération", i, "terminée.")
    print("continue")