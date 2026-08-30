def calc_Beam_volume(Width ,length ,height ):
    """
    Calculate the volume of the rectangular Beam 

    args:
        Width(float):Width of the retangular beam.
        length(float):length of the rectangular beam.
        height(float):height of the rectangular beam.
    returns:
        float:Volume of the rectangular beam. 
    """
    return Width * length * height

if __name__=="__main__":
    Width = float(input("enter Width: "))
    length = float(input("enter length: "))
    height = float(input("enter height"))
    volume = calc_Beam_volume(Width ,length ,height )
    print("Volume = ",volume )