from abc import abstractmethod, ABCMeta
from math import pi
from math import sqrt


class Formes_Geometrique: 
    """La classe de base abstraite""" 
    def __init__(self,surface,perimetre):
        self.surface = surface
        self.perimetre = perimetre  

    @abstractmethod
    def perimetre(self, perimetre):
        return self.perimetre    
    
    @abstractmethod 
    def surface(self, surface):       
       return self.surface
        

    
class Rectangle(Formes_Geometrique):
    """création de la classe Triangle qui hérite de la classe Formes_Geometrique et son constructeur"""
    def __init__(self,longueur, largeur):
            self.L = longueur
            self.l = largeur
        
class Cercle(Formes_Geometrique):
    """création de la classe Cercle qui hérite de la classe Formes_Geometrique et son constructeur"""
 
    def __init__(self, rayon):
        self.r = rayon
        
class Triangle(Formes_Geometrique):
    """création de la classe Triangle qui hérite de la classe Formes_Geometrique et son constructeur"""
    def __init__(self,cote_a,cote_b,cote_c):
        self.a = cote_a
        self.b = cote_b 
        self.c = cote_c 
        