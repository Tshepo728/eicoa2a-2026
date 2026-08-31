safety_margin = 1.5
def apply_local_threshold(value):
    """
    Calculate threshold value using safety margin
    Args:
        value(float) = safety measure
    returns:
        float :calculated safety tthreshold 
    """
    safety_margin = 2.50
    results = value * safety_margin
    return results

if __name__=="__main__":
    value = float(input("enter value: "))
    results = apply_local_threshold(value)
    print(f"local safety margin = {results :.2f} ")
    print(f"global safety margin = {safety_margin :.2f} ")