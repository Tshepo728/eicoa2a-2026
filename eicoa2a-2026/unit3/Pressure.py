def calc_pressure(force , Area):
    """
    Calculate pressure exerted on a hydraulic piston head

    Args:
        force(float):force exerted on the hydraulic piston in newtons(N)
    
        Area(float)::Area of the hydraulic piston in square metres(m**2)
    returns:
        float:Pressure exerted on a hydraulic piston         
    """

    return force / Area

if __name__=="__main__":
    force = float(input("enter force(N): "))
    Area = float(input("enter area(m**2): "))
    Pressure = calc_pressure(force ,Area)
    print("Pressure = ",Pressure ,"Pa")