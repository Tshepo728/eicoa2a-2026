from resistor import Resistor

resistor1 = Resistor(4, 12) 
resistor2 = Resistor(6, 24)

print("Resistor 1") 
print("Resistance:", resistor1.Resistance_ohms, "ohms") 
print("Voltage:", resistor1.voltage, "volts") 
print("Current:", resistor1.calc_current(), "A")

print()

print("Resistor 2") 
print("Resistance:", resistor2.Resistance_ohms, "ohms") 
print("Voltage:", resistor2.voltage, "volts") 
print("Current:", resistor2.calc_current(), "A")


