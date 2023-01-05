from question_4 import *

class Forme_exploitateur:
    def __init__(self):
        self.longueur = longueur
        self.largeur = largeur

    def surface_rectangle(self):
        rectangle = Rectangle(self.longueur,self.largeur)
        return rectangle.surface()

    def perimetre_rectangle(self):
        rectangle = Rectangle(self.longueur, self.largeur)
        return rectangle.perimetre()

 # Principal        
longueur = float(input("Entrer la valeur de la longueur: "))
largeur = float(input("Entrer la valeur de la largeur: "))
demo_1 = Forme_exploitateur()
print(f"Le perimetre vaut : {demo_1.perimetre_rectangle()} m")
print(f"La surface vaut: {demo_1.surface_rectangle()} m²")