from sensor_utils import celcius_to_fharenheit
temperatures =[20, 25, 46, 16,]

for celcius in temperatures:
    Fharenheit = celcius_to_fharenheit(celcius)

    print(f"Celsius: {celcius} C") 
    print(f"Fahrenheit: {Fharenheit:.2f}F") 
    print()

