readings = [12.6, 12.4, 12.8, 11.9, 12.5]
print("ALL READINGS :", readings)
print("first reading : ", readings[0])
print("last readding :", readings[-1])
readings.append(12.7)
print("UPDATED READINGS :", readings)
readings[1] = 12.3
print("UPDATED READINGS :", readings)
total = sum(readings)
average = total / len(readings)
print("Total of readings : ", total)
print("Average of readings : ", average)