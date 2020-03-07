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
        return "I am the {} dog, age: {}, weight: {}.".format(self.name, self.age, self.weight)
    
class AssistantDog(Dog):
    def __init__(self, name, age, weight, owner):
        Dog.__init__(self, name, age, weight)
        self.owner = owner
        self.__working = False # Para saber si está walking.
        
    def __str__(self): # Definición de cómo quiero que se muestren las instáncias de esta clase.
        return "I am the {} assistant dog, owner: {}.".format(self.name, self.owner)
    
    def walk(self):
        print("I help my owner to have a walk")
        
    def shout(self):
        if self.working:
            print("Shut Up, I cannot shout!")
        else:
            Dog.shout(self)
            
    def working(self, isWorking = None): # Hacemos que sea un atributo privado, pero insantdo accedemos (Dog.AssistantDog.__working() ) 'getter'
        if isWorking == None:
            return self.__working
        
        else:
            self.__working = isWorking # Si Dog.AssistantDog.__working(True) is 'setter'. Overwritting.
        
        