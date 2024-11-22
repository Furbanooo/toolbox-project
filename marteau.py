from outil import Outil

class Marteau(Outil):
    def __init__(self, taille):
        super().__init__(type_outil="Marteau", sous_type=None, taille=taille)

    def planter_clou(self):
        self.utiliser()
        print("Le marteau plante un clou.")
