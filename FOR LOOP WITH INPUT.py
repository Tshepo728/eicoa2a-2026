Total = 0
invalid_count = 0

for i in range(5):
    while True:
        voltage = float(input("enter battery voltage: "))
        if 0 <= voltage <= 15:
            Total += voltage
            break
        else:    
            print("invalid reading entered enter a number between 0 and 15")
            invalid_count += 1

average = Total / 5

print("Average voltage:", average)
print("Invalid readings entered:", invalid_count)  



