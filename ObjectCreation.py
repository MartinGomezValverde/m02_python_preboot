#Creación de un objeto.

class Dog():
    def __init__(self, name, age, weight): # Función constructora.
        self.name = name
        self.age = age
        self.weight = weight
        
    def shout(self):# Siempre primero self.
        if self.weight >= 8:
            print("GUAU, GUAU")
            
        else:
            print("guau, guau")
            
    def __str__(self): # Definición de cómo quiero que se muestren las instáncias de esta clase.
        return "I am the {} dog.".format(self.name)
        
        