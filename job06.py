class Rectangle: 
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur

    def __str__(self):
        return f"Rectangle: longueur={self.__longueur}, largeur={self.__largeur}"
    
rectangle = Rectangle(10, 5)
print(rectangle)

rectangle.set_longueur(15)
rectangle.set_largeur(8)
print(rectangle)
    