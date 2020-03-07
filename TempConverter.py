class Thermometer():
    def __init__(self):
        self.__unit = "C"
        self.__temperature = 0
        
    def __converter(self, unit, temperature):
        if unit == "C":
            return "{}º F".format(temperature * 9/5 + 32)
            
        elif unit == "F":
            return "{}º C".format(temperature - 32 * 5/9)
        
        else:
            return "Incorrect unit"
        
    def __str__(self):
        return "{}º {}".format(self.temperature, self.unit)
    
    def unit(self, uni = None):
        if uni == None:
            return self.__unit
        else:
            if uni == "F" or uni == "C":
                self.__unit = unit
                
    def temp(self, temperature = None):
        if temperature == None:
            return self.__temperature
        else:
            self.__temperature = temperature
            
    def mesure(self, uni = None):
        if uni == None or uni == self.__unit:
            return self.__str__()
        else:
            return self.converter(self.__temperature, self.__unit)
        