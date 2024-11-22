import csv
from datetime import datetime
from tournevis import Tournevis
from marteau import Marteau
from cleplate import ClePlate
from perceuse import Perceuse
from foret import Foret

# Fonction pour charger les outils depuis le fichier CSV
def charger_boite(fichier):
    boite = []
    with open(fichier, mode='r') as file:
        csv_reader = csv.DictReader(file, delimiter=';')
        for ligne in csv_reader:
            type_outil = ligne["Type"]
            sous_type = ligne["sous-type"]
            taille = ligne["taille"]
            etat = ligne["Etat"]
            emprunteur = ligne["Emprunt"]
            date_emprunt = ligne["date emprunt"]
            usage = int(ligne["usage"])
            
            if type_outil == "Tournevis":
                outil = Tournevis(sous_type, taille)
            elif type_outil == "Marteau":
                outil = Marteau(taille)
            elif type_outil == "Clé plate":
                outil = ClePlate(taille)
            elif type_outil == "Perceuse":
                outil = Perceuse(taille)
            elif type_outil == "Foret":
                outil = Foret(taille)
            else:
                continue

            outil.etat = etat
            outil.emprunteur = emprunteur
            outil.date_emprunt = date_emprunt
            outil.usage = usage
            boite.append(outil)
    return boite

# Fonction pour enregistrer l'état de la boîte dans un fichier CSV
def sauvegarder_boite(boite, fichier):
    with open(fichier, mode='w') as file:
        fieldnames = ['Type', 'sous-type', 'taille', 'Etat', 'Emprunt', 'date emprunt', 'usage']
        writer = csv.DictWriter(file, delimiter=';', fieldnames=fieldnames)
        writer.writeheader()
        for outil in boite:
            writer.writerow({
                "Type": outil.type_outil,
                "sous-type": outil.sous_type,
                "taille": outil.taille,
                "Etat": outil.etat,
                "Emprunt": outil.emprunteur,
                "date emprunt": outil.date_emprunt,
                "usage": outil.usage
            })

# Menu principal
def menu_principal(boite):
    while True:
        print("\nMenu Principal")
        print("1. Lister les outils")
        print("2. Emprunter un outil")
        print("3. Restituer un outil")
        print("4. Utiliser un outil")
        print("5. Créer le fichier d'état de la boîte")
        print("6. Quitter")

        choix = input("Votre choix : ")
        if choix == "1":
            for outil in boite:
                print(f"{outil.type_outil} {outil.sous_type or ''} - Taille: {outil.taille} - État: {outil.etat}")
        elif choix == "2":
            emprunter_outil(boite)
        elif choix == "3":
            restituer_outil(boite)
        elif choix == "4":
            utiliser_outil(boite)
        elif choix == "5":
            sauvegarder_boite(boite, "newtoolbox.csv")
            print("État de la boîte sauvegardé.")
        elif choix == "6":
            print("Au revoir.")
            break
        else:
            print("Choix invalide.")

# Gestion des emprunts
def emprunter_outil(boite):
    type_outil = input("Quel type d'outil voulez-vous emprunter ? (Tournevis/Marteau/Clé plate/Perceuse/Foret) : ")
    taille = input("Indiquez la taille : ")
    for outil in boite:
        if outil.type_outil == type_outil and outil.taille == taille and outil.etat == "disponible":
            nom = input("Nom de l'emprunteur : ")
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if outil.emprunter(nom, date):
                print(f"{type_outil} emprunté avec succès.")
            return
    print("Outil non disponible ou introuvable.")

# Gestion des restitutions
def restituer_outil(boite):
    type_outil = input("Quel type d'outil voulez-vous restituer ? : ")
    taille = input("Indiquez la taille : ")
    for outil in boite:
        if outil.type_outil == type_outil and outil.taille == taille and outil.etat == "emprunté":
            if outil.restituer():
                print(f"{type_outil} restitué avec succès.")
            return
    print("Outil non trouvé ou déjà disponible.")

# Utilisation d'un outil
def utiliser_outil(boite):
    type_outil = input("Quel type d'outil voulez-vous utiliser ? : ")
    taille = input("Indiquez la taille : ")
    for outil in boite:
        if outil.type_outil == type_outil and outil.taille == taille:
            if outil.etat != "emprunté":
                print("Outil non emprunté, impossible de l'utiliser.")
                return
            if type_outil == "Tournevis":
                action = input("Voulez-vous visser ou dévisser ? : ")
                if action == "visser":
                    outil.visser()
                elif action == "dévisser":
                    outil.devisser()
            elif type_outil == "Marteau":
                outil.planter_clou()
            elif type_outil == "Perceuse":
                outil.percer()
            else:
                print(f"Utilisation non définie pour {type_outil}.")
            return
    print("Outil non trouvé.")

# Point d'entrée
if __name__ == "__main__":
    boite_outils = charger_boite("toolbox.csv")
    menu_principal(boite_outils)
