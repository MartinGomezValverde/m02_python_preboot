#Creación de un objeto.

class Dog():
    def __init__(self, name, age, weight): # Función constructora.
        self.name = name
        self.age = age
        self.weight = weight
        
    def shout(self)# Siempre primero self.
        print("Guau, guau")
        
        