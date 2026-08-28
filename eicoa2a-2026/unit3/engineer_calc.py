from ohms_law import calc_resistance ,calc_power
from unit_converter import inches_to_mm ,mm_to_inches ,cm_to_inches ,inches_to_cm

def display_menu():
    """
    print a numbered menu of engineering calculations.

    the menu includes:
    1.calculate resistane 
    2.convert length 
    3.calculate power
    4.Exit
    """
    print("\n---engineering calculator---")
    print("1.calculate resistance")
    print("2.convert length ")
    print("3.calculate power")
    print("4.Exit")

def main():
    running = True
    while running:
        display_menu()

        choice = input("select an option")
        if choice == "1":
            voltage=float(input("enter measured voltage(v): "))
            current = float(input("enter current(A): "))
            resistance = calc_resistance(voltage, current)

            print("Resistance = ",resistance ,"ohms")
        elif choice == "2":

            direction =input("enter conversion :(inches_to_mm / mm_to_inches / cm_to_inches / inches_to_cm ) ")
            value = float(input("enter measurement: "))
            if direction == "inches_to_mm":
                results = inches_to_mm(value)
                print("Converted value",results ,"mm")
            elif direction == "mm_to_inches":
                results = mm_to_inches(value)
                print("Converted value" , results ,"inches")
            elif direction == "cm_to_inches":
                results = cm_to_inches(value)
                print("Converted value",results ,"inches")
            elif direction == "inches_to_cm":
                results = inches_to_cm(value)
                print("Converted value",results ,"cm")
            else:
                print("invalid conversion")
        elif choice == "3":
            voltage = float(input("enter voltage: "))
            resistance = float(input("enter resistance"))
            POWER = calc_power(voltage ,resistance)

            print("POWER = ",POWER ,"Watts")

        elif choice == "4":
            print("User exited.")
            running = False

        else:
            print("invalid option")

if __name__=="__main__":
    main()
        
                    

            
            




      
