def calc_pressurec(force , Area):
    """
    Calculate pressure exerted on a hydraulic piston head

    Args:
        force(float):force exerted on the hydraulic piston in newtons(N)
    
        Area(float)::Area of the hydraulic piston in square metres(m**2)
    returns:
        float:Pressure exerted on a hydraulic piston         
    """
    force =float(input("enter force(N)"))
    Area = float(input("enter area(m**2)"))
    return force / Area
    