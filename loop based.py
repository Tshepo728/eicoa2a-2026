GOOD = 0
MARGINAL = 0
LOW = 0
invalid_value=0


N =int(input("enter number of batteries :"))
for i in range (N):
    while True:
     voltage = float(input("enter battery voltage : "))     
    if 0 <= voltage <= 15:
            if voltage > 12.5:
                 GOOD += 1
                 print("GOOD")
            elif voltage >=11.5:
                MARGINAL += 1
                print("MARGINAL")
            else:
                LOW += 1
                print("LOW")
            break
    else:
            invalid_value += 1
            print("invalid battery value")

print("number of good batteries : ", GOOD)
print("number of marginal batteries : ", MARGINAL)
print("number of low batteries : ", LOW)
print("number of invalid battery values : ", invalid_value)

