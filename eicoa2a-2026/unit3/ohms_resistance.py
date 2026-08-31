def calc_resistance(voltage ,current):
    """
    Calculate Resistance using ohm's law
    
    Args:
        voltage : voltage across the circuit(V).
        current : current flowing in the circuit(A).Must be non-zero.
    Returns:
        float: resistance in ohms
    """
    if current == 0:
        return 0.0
    else:
        resistance = voltage / current 
        return resistance 


if __name__=="__main__":
    voltage = float(input("enter voltage(V): "))
    current = float(input("enter current(A): "))
    resistance = calc_resistance(voltage ,current)
    print("Resistance",resistance ,"ohms")
