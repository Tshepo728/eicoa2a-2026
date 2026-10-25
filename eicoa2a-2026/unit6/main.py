from resistor import Resistor

resistor1 = Resistor(4, 12) 
resistor2 = Resistor(6, 24)

print("Resistor 1") 
print("Resistance:", resistor1.resistance_ohms, "ohms") 
print("Voltage:", resistor1.voltage, "volts") 
print("Current:", resistor1.calculate_current(), "amperes")


