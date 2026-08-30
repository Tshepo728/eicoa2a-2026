def calc_flow_rate(volume , time):
    """
    Calculate flow rate using volume in litres and time in seconmds
    Args:
        volume(float): volume in litres(L)
        time(float):time taken in seconds(s)
    returns:
        float:flow rate (L/s)
    """
    return volume / time
if __name__=="__main__":
    volume = float(input("enter volume in litres : "))
    time = float(input("enter time in seconds"))
    results = volume / time
    print(f"flowrate = {results :.2f}")
    print("\n---flow rate documentation---")
    print(calc_flow_rate. __doc__)