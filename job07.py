class Livre:
    def __init__(self, title, author, nbr_pages ):
        self.__title = title
        self.__author = author
        self.__nbr_pages = nbr_pages

    def get_title(self):
        return self.__title
    
    def set_title(self, newtitle):
        self.__title = newtitle

    def get_author(self):
        return self.__author
    
    def set_author(self, newauthor):
        self.__author = newauthor

    def get_nbr_pages(self):
        return self.__nbr_pages
    
    def set_nbr_pages(self, newnbr_pages):
        if isinstance(newnbr_pages, int) and newnbr_pages > 0:
            self.__nbr_pages = newnbr_pages
        else: 
            print("Erreur : Le nombre de pages doit être un nombre entier positif.")
    
    def __str__(self):
        return f"Livre : titre ='{self.__title}', auteur ='{self.__author}', nombre de pages ='{self.__nbr_pages}'"

livre = Livre("Coder pour les nuls", "Alain Chabat", 137)

livre.set_nbr_pages(-17)
print(livre)


