class Resistor:
    def __init__(self, Resistance_ohms, voltage):
        self.Resistance_ohms = Resistance_ohms
        self.voltage = voltage

    def calc_current(self):
            return self.voltage / self.Resistance_ohms
        

    
