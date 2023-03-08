
class ArrayStack:
    """LIFO stack implementation using
    a python list as underlying storage"""
    def __init__(self):
        """ create an empty stack"""
        self._data = []
        
    def __len__(self):
        """ Return the number of
        elements in the satck""" 
        return len(self._data)
    
    def is_empty(self):
        """Return True if the stack is empty"""
        return len(self._data) == 0
    
    def push(self, e):
        """ Return but not remove the
        element at the top of the stack"""
        self._data.append(e)
        
    def top(self):
        """Return (but not remove) the element
        at the top of the stack
        Raise empty Exception if the stack is empty"""
        if self.is_empty():
            return 'Stack is empty'   # Ajout 
            #raise Empty('Stack is empty')
        return self._data[-1]
    
    def pop(self):
        """Remove and return the element
        form the top of the stack LIFO.
        Raise Empty exception if the stack is emmpty"""
        if self.is_empty():
            return 'Stack is empty'   # Ajout 
            #raise Empty('Stack is empty')
        return self._data.pop()
    
        
if __name__ == '__main__':
    # Création d'une nouvelle pile vide
    liste = ArrayStack()
    # Affichons la taille de la pile créée
    print(f"\nLanouvelle taille de la liste vaut: ---> {len(liste)}")
    
    # Vérifions le contenu de la pile 
    print(f"\nIs the stack empty?: ---> {liste.is_empty()}" )
    
    # Ajoutons des éléments dans notre pile
    
    liste.push(17)
    liste.push(11)
    liste.push(2000)
    liste.push(28)
    liste.push(5)
    liste.push(2001)
    liste.push(24)
    liste.push(7)
    liste.push(2002)
    
    # Affichons la nouvelle taille de la pile
    print(f"\nLa nouvelle taille de la liste vaut: ---> {len(liste)}")
    
    # Référence de l'élément au top
    print(f"\nL'élément au top de notre pile est: ---> {liste.top()}" )
    
    # Suprimons l'élément au top ---> 2002, puis affichons la taille
    liste.pop()
    print(f"\nLa nouvelle taille de la liste vaut: ---> {len(liste)}" )
    
    # Suprimons l'élément au top ---> 7 sachant qu'on a déjà supprimé 2002 puis affichons la taille
    
    liste.pop()
    print(f"\nLa nouvelle taille de la liste vaut: ---> {len(liste)}" )
    
    # Vérifions le contenu de la pile 
    print(f"\nIs the stack empty?: --->{liste.is_empty()}")
    
    liste.pop()
    liste.pop()
    liste.pop()
    liste.pop()
    liste.pop()
    liste.pop()
    liste.pop()
    
    print(f"\nIs the stack empty?: --->{liste.is_empty()}")




    
    
    
    
    
    
    
    
    
        
    
        
