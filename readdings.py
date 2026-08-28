total = 0
for i in range (5):
    measurements = float(input("enter measured value: "))
    total += measurements

average = total / 5
print("total average: ", average)

total = 0
count = 0
while count < 5:
    measurements = float(input("enter measured value: "))
    total += measurements
    count += 1

average = total / 5
print("total average :" ,average)