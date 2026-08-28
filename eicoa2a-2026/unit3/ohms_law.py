def calc_resistance(voltage, current):
    """
    Calculate resistance using ohm's law.
    
    Args:
        voltage(float):voltage across the component in volts(v).
        current(float):current across the component in Amperes(A).
        returns:
            float:resistance in ohms
            """
    return  voltage / current 

# Exercise 1 :POWER
def calc_power(voltage, resistance):
    """
    Calculate Power dissipated in a resistor
    
    Args:
        voltage(float):voltage across the component in volts(v).
        resitance(float):resistance of the component in ohms.
        returns:
            float:Power in Watts
            """
    current = voltage / resistance 
    return  voltage * current


