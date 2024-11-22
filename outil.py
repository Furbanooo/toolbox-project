class Outil:
    def __init__(self, type_outil, sous_type, taille, etat="disponible", emprunteur=None, date_emprunt=None, usage=0):
        self.type_outil = type_outil
        self.sous_type = sous_type
        self.taille = taille
        self.etat = etat
        self.emprunteur = emprunteur
        self.date_emprunt = date_emprunt
        self.usage = usage

    def emprunter(self, nom_emprunteur, date):
        if self.etat == "emprunté":
            return False
        self.etat = "emprunté"
        self.emprunteur = nom_emprunteur
        self.date_emprunt = date
        return True

    def restituer(self):
        if self.etat == "disponible":
            return False
        self.etat = "disponible"
        self.emprunteur = None
        self.date_emprunt = None
        return True

    def utiliser(self):
        if self.etat == "disponible":
            raise Exception("L'outil doit être emprunté pour être utilisé.")
        self.usage += 1
