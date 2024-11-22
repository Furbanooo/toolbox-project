from outil import Outil

class Perceuse(Outil):
    def __init__(self, taille):
        super().__init__(type_outil="Perceuse", sous_type=None, taille=taille)

    def percer(self):
        self.utiliser()
        print("La perceuse perce un trou.")
