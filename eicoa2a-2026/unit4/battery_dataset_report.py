good = 0
marginal = 0
low = 0
low_readings = []

voltages = [12.8, 11.4, 12.1, 10.9, 12.7, 11.8, 13.0, 11.2]
print("highest voltage:", voltages[6])
print("lowest voltage:", voltages[3])

for voltage in voltages:
    if voltage >= 12.5:
        status = "good"
        good += 1
    elif voltage >= 11.5:
        status = "marginal"
        marginal += 1
    else:
        status ="low"
        low += 1
        low_readings.append(voltage)

        print(voltage , status)

total = sum(voltages)
Average = total / len(voltages)
print("total voltages:", total)
print("Total voltage:", total)
print("good readings:", good)
print("marginal readings:", marginal)
print("low readings:", low)
print("all low readings:", low_readings)