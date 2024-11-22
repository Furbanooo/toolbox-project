from outil import Outil

class Tournevis(Outil):
    def __init__(self, sous_type, taille):
        super().__init__(type_outil="Tournevis", sous_type=sous_type, taille=taille)

    def visser(self):
        self.utiliser()
        print("Le tournevis visse.")

    def devisser(self):
        self.utiliser()
        print("Le tournevis dévisse.")
