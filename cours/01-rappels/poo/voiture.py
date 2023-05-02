class Voiture:
    def __init__(self, marque, couleur):
        print("Appel du constructeur")
        self.marque = marque
        self.couleur = couleur

    def repeindre(self, nouvelle_couleur):
        self.couleur = nouvelle_couleur

    def __str__(self):
        return f"Je suis une voiture de marque {self.marque} et de couleur {self.couleur}."

    def __gt__(self, other):
        return len(self.marque) > len(other.marque)

    def __eq__(self, other):
        return self.marque == other.marque

    def __lt__(self, other):
        return True

    def __len__(self):
        return len(self.couleur)

class Velo:
    def __init__(self, marque):
        self.marque = marque

tesla_rouge = Voiture("Tesla", "Rouge")
mercedes = Voiture("Mercedes", "Rouge")
velo = Velo("Tesla")
# print(tesla_rouge.couleur)
# tesla_rouge.repeindre("Vert")
# print(tesla_rouge.couleur)
print(tesla_rouge)
print(tesla_rouge > velo)
