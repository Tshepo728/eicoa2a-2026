temperature = float(input("enter temperature reading : "))
attempts = 0
warnings = 0
while temperature != -1 and temperature >= 40:
    attempts += 1
    warnings += 1
    print ("WARNING : temperature is too high")
    temperature = float(input("enter temperature reading : "))

if temperature == -1:
    print ("program terminated by user")

print("number of attempts : ",attempts )
print("number of warnings :", warnings )    
