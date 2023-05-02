# On peut importer sur plusieurs lignes.
# Privilégier import module pour importer les modules intégrés.
import sys
import os

# Pour les autres modules, privilégier la syntaxe from module import function


# 2 lignes vide pour séparer les classes du reste
class MyClass():
    def __init__(self):
        pass
    # à l'intérieur d'une classe, séparer les méthodes avec une ligne vide.

    def method_1(self):
        pass


# deux lignes vides après.

# Docstring pour expliquer des classes, fonctions etc.
# A mettre en début de classe/méthode.
def main(a, b):
    """
        Super fonction qui retourne a et b.
        :param a: un nombre:
        :param b: un nombre
        :return: un tuble (a, b).
    """

    # On peut faire des commentaires multignes comme ceci
    # Ligne 2
    # blablbla

    return a, b

print(main.__doc__)