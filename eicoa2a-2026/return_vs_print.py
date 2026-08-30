def mm_to_inches(mm):
    """
    Convert mm_to_inches
    Args:
        millimetres: length in millimetres(mm).
    returns:
        float:length in inches.
    """
    return mm /25.4

if __name__=="__main__":
    value: float = float(input("enter length in millimetres: "))
    inches = mm_to_inches(value)
    print("Converted value = ",inches)

