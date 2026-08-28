readings = [8.2, 8.5, 8.1, 8.3, 8.4]
total = 0
for readings in readings:
    total += readings

average = total / 5 
print("AVERAGE :" ,average)    

readings = []
total = 0 
while len(readings) < 5:
    reading = float(input("enter readding : "))

    if 0 <= reading <= 10:
     readings.append(reading) 
    total += reading

else: 
   print ("invalid reading") 

average = total / 5
print("average is: ", average)