from outil import Outil

class ClePlate(Outil):
    def __init__(self, taille):
        super().__init__(type_outil="Clé plate", sous_type=None, taille=taille)
