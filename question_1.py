from abc import abstractmethod, ABCMeta
from math import pi
from math import sqrt



class Formes_Geometrique:  
    
    def __init__(self,surface,perimetre):
        self.surface = surface
        self.perimetre = perimetre  

    @abstractmethod
    def perimetre(self, perimetre):
        return self.perimetre    
    
    @abstractmethod 
    def surface(self, surface):       
       return self.surface
        
