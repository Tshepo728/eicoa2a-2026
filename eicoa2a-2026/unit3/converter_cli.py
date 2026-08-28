from unit_converter import inches_to_mm ,mm_to_inches ,cm_to_inches ,inches_to_cm
direction = input("enter conversion,(inches_to_mm / mm_to_inches / cm_to_inches / inches_to_cm): ")
value = float(input("enter measurement: "))
if direction == "inches_to_mm":
    results = inches_to_mm(value)
    print("Converted value :", results ,"mm")
elif direction == "mm_to_inches":
    results = mm_to_inches(value)
    print("Converted value :", results ,"inch")
elif direction == "cm_to_inches":
    results = cm_to_inches(value)
    print("Converted value :", results ,"inches")
elif direction == "inches_to_cm":
    results = inches_to_cm(value)
    print("Converted value :", results ,"cm") 

else:
    print("invalid conversion option")

print(inches_to_mm.__doc__)
print(mm_to_inches.__doc__)
print(cm_to_inches.__doc__)
print(inches_to_cm.__doc__)