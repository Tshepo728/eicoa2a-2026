temperature_limit = (10 ,80)
minimum_temperature , maximum_temperature = temperature_limit
measured_temperature = float(input("Enter the measured temperature: "))
if minimum_temperature <= measured_temperature <= maximum_temperature:
    print("within range")
else:
    print("outside range")

