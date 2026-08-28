def mm_to_inches(mm):
    """
    convert millimetres(mm) to inches(n).
    Args:
        length in millimetres.
    return:
         float: length in inches(n) (1 inch = 25.4 mm)
         """
    return mm / 25.4

def inches_to_mm(inches):
    """
    convert millimetres(mm) to inches(n).
    Args:
        inches(float):length in millimetres.
    
    return:
        float:length in millimetres (inches * 25.4 mm)
    """
    return inches * 25.4

# Exercise 2 : Unit Converter
def cm_to_inches(cm):
    """
    convert centimetres(cm) to inches(n).
    Args:
        centimetres(float):length in centimetres(cm).
    
    return:
        float:length in inches (1 inch = 2.54 cm)
    """
    return cm / 2.54

def inches_to_cm(inches):
    """
    convert inches to centimetres.
    Args:
        inches(float):length in inches
    
    return:
        float:length in centimetres
    """
    return inches * 2.54