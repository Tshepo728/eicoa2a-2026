total = 0
invalid_count =0

for i in  range (1,6):
    while True:
        voltage = float(input("enter battery voltage:" ))
        if 0 <= voltage <= 15:
            total += voltage
            break
        else:
            print("invalid reading entered enter a number between 0 and 15")
            invalid_count += 1


average = total / 5

print ("AVERAGE READING IS : ", average )
print (" NUMBER OF INVALID READINGS : " ,invalid_count )  