voltage = [12.6, 12.4, 12.8, 11.9, 12.5]

print(voltage[0])
print(voltage[-1])
voltage.append(12.7)
print(voltage)
voltage[3] = 12.1
print(voltage[:3])
print(voltage)
total =sum(voltage)
average = total/ len(voltage)
print("total voltage:", total)
print("average voltage:", average)