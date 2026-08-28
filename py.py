good = 0
marginal = 0 
low = 0
invalid_value = 0

N = int(input("enter number pf batteries : "))
for i in range (N):
    while True:
        voltage = float(input("enter battery voltage :"))
        if 0 <= voltage <= 15:
            if voltage > 12.5:
               good += 1
                print("good")
            elif voltage >= 11.5:
                   marginal += 1
                print("marginal")
        else:
            low += 1
            print("low")

        break
    else:
        invalid_value += 1
        print("invalid battery value, enter a number between 0 and 15")

print("number of good batteries : ", good)
print("number of marginal batteries : ", marginal)
print("number of low batteries : ", low)
print("number of invalid battery values : ", invalid_value)

      