from abc import abstractmethod, ABCMeta
from math import pi
from math import sqrt



class Formes_Geometrique:  
    
    def __init__(self,surface,perimetre):
        self.s = surface
        self.p = perimetre  

    @abstractmethod
    def perimetre(self, perimetre):
        return self.perimetre    
    
    @abstractmethod 
    def surface(self, surface):       
       return self.surface
        

    
class Rectangle(Formes_Geometrique):
       
    def __init__(self,longueur, largeur):
        if (largeur >=0  and longueur >=0):
            self.L = longueur
            self.l = largeur 
        else:
            self.L= abs(longueur)
            self.l= abs(largeur)
        
    def surface(self):
            return self.L * self.l
        
            
    def perimetre(self):
        return (self.L + self.l)*2

    def result_rectangle(self):
        if (self.L == self.l):
            print(f"Pour le carré de côté c = {self.L} m :")
            print(f"    Le perimètre du rectangle vaut: {self.perimetre()} m")
            print(f"    La surface du rectangle vaut: {self.surface()} m²\n\n")
        
        else:
            print(f"Pour le rectangle de longueur L={self.L} m et largeur l={self.l} m :")
            print(f"    Le perimètre du rectangle vaut: {self.perimetre()} m")
            print(f"    La surface du rectangle vaut: {self.surface()} m²\n\n")
        
        
        
    @classmethod 
    def Carre(cls,mesure_cote):
        return cls(mesure_cote,mesure_cote)
    
        
class Cercle(Formes_Geometrique): 
    def __init__(self, rayon):
        if rayon >= 0:
            self.r = rayon  
        else:
             self.r= abs(rayon)

    def perimetre(self):
        #return "{:.3f}".format(2*pi*self.r)
        return 2*pi*self.r

        
    
    def surface(self):        
        return "{:.3f}".format(pi*(self.r)**2)

    def result_cercle(self):
        print(f"\n\nPour le cercle de rayon R ={self.r} m")
        print(f"    Le perimètre du celcle vaut: {self.perimetre()} m")
        print(f"    La surface du celcle vaut: {self.surface()} m²\n\n")
        
        
class Triangle(Formes_Geometrique):
    
    def __init__(self,cote_a,cote_b,cote_c):
        if cote_a >=0 and cote_b >= 0 and cote_c >= 0:
            self.a = cote_a
            self.b = cote_b 
            self.c = cote_c         
        else:
            self.a = abs(cote_a)
            self.b = abs(cote_b)
            self.c = abs(cote_c)
    
    def perimetre(self):
        return self.a + self.b + self.c
   
    def surface(self):
        dem_p = (self.a+self.b+self.c)/2
        surface = sqrt(abs(dem_p*(dem_p-self.a)*(dem_p-self.b)*(dem_p-self.c)))
        return "{:.3f}".format(surface)
    
    def result_triangle(self):
        if (self.c == sqrt((self.a)**2 + (self.b)**2)):
            print(f"Pour le triangle rectangle de hauteur a={self.a}m et de base b={self.b}m :")
            print("    Le perimètre du triangle vaut: {:.3f} m".format(self.perimetre()))
            print("    La surface du triangle vaut: {} m²\n\n".format(self.surface()))
        else:
            print(f"Pour le triangle des côtés a={self.a}m, b={self.b}m et c={self.c}m:")
            print("    Le perimètre du triangle vaut: {:.3f} m".format(self.perimetre()))
            print(f"    La surface du triangle vaut: {self.surface()} m²\n\n")

    @classmethod    
    def Rectangle(cls, a, b):
        return cls(a,b, sqrt(a**2 + b**2))