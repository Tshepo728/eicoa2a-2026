voltages = [12.8, 11.4, 12.1, 10.9, 12.7, 11.8, 13.0, 11.2]
print("highest reading :", max(voltages))
print("lowest reading :", min(voltages))
good = 0
marginal = 0 
low = 0
low_readings = []

def classify_voltage(voltages):
    global good , marginal , low
    for voltage in voltages:
        if voltage > 12.5:
            good += 1
        elif 11.5 <= voltage <= 12.5:
            marginal += 1
            
        else:
            low += 1
            low_readings.append(voltage)

def calc_average(voltages):
        return sum(voltages) / len(voltages)
classify_voltage(voltages)
print("good :", good)
print("marginal :", marginal)
print("low :", low)
print("low readings :", low_readings)
print("average voltage :", calc_average(voltages))
        