class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def se_presenter(self):
        print("Je suis", self.nom, self.prenom)
    
personne1 = Personne("John", "DOE")
personne2 = Personne("Jean","DUPOND")

personne1.se_presenter()
personne2.se_presenter()
