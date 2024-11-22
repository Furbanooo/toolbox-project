from outil import Outil

class Foret(Outil):
    def __init__(self, taille):
        super().__init__(type_outil="Foret", sous_type=None, taille=taille)

    def percer(self, perceuse):
        if perceuse.type_outil != "Perceuse":
            raise Exception("Un forêt ne peut être utilisé qu'avec une perceuse.")
        self.utiliser()
        perceuse.utiliser()
        print("Le forêt perce un trou avec la perceuse.")
