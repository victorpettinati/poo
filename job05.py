class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""
    
    def vieillir(self):
        self.age += 1
    
    def nommer(self):
         self.prenom = "Luna"   

animal = Animal()
prenom = "Luna"

print("L'animal se nomme", prenom)
print("Âge de l'animal: ", animal.age)

animal.vieillir()

print("Âge de l'animal après viellissement :", animal.age)








    


