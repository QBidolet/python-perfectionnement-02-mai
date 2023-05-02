from voiture import Voiture


class VoitureDeCourse(Voiture):
    def __init__(self, couleur, marque, vitesse):
        Voiture.__init__(self, couleur, marque)
        self.vitesse = vitesse

    def __str__(self):
        return f'Je suis une voiture {self.marque} ' \
               f'de couleur {self.couleur} ' \
               f'vitesse: {self.vitesse} km/h'


ma_ferrari = VoitureDeCourse('Rouge', 'Ferrari', 300)
print(ma_ferrari)
