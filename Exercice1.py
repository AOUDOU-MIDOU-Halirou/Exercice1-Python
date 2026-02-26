class Biscuit:
    # creation du constructeur de la classe Biscuit
    #  avec ses deux attributs nom et forme
    def __init__(self, nom, forme):
        self.nom = nom
        self.forme = forme
    
    # creation d'une methode cuir qui affiche deux phrases
    def cuir(self):
        print(f"Ce {self.nom} a été cuit sous la forme d'une {self.forme}.")
        print("Bonne dégustation.")
    
    #creation d'un objet
biscuit1 = Biscuit("cookie pépite de chocolat", "étoile")
biscuit1.cuir()
