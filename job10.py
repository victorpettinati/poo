class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, en_marche=False, reservoir=50):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = en_marche
        self.__reservoir = reservoir

    def get_marque(self):
        return self.__marque

    def set_marque(self, marque):
        self.__marque = marque

    def get_modele(self):
        return self.__modele

    def set_modele(self, modele):
        self.__modele = modele

    def get_annee(self):
        return self.__annee

    def set_annee(self, annee):
        self.__annee = annee

    def get_kilometrage(self):
        return self.__kilometrage

    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    def demarrer(self):
        if self.__verifier_plein():
            self.__en_marche = True
        else:
            print("Le réservoir est presque vide, veuillez faire le plein avant de démarrer.")

    def arreter(self):
        self.__en_marche = False

    def __verifier_plein(self):
        return self.__reservoir > 51
    
    def afficher_info(self):
        print(f"Marque: {self.__marque}")
        print(f"Modèle: {self.__modele}")
        print(f"Année: {self.__annee}")
        print(f"Kilométrage: {self.__kilometrage}")
        print(f"En marche: {self.__en_marche}")
        print(f"Réservoir: {self.__reservoir}")

# Exemple d'utilisation
voiture = Voiture("Toyota", "Corolla", 2015, 60000)
voiture.demarrer()
voiture.afficher_info()
voiture.arreter()
voiture.afficher_info()