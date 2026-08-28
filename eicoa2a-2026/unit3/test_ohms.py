from ohms_law import calc_resistance, calc_power

results = calc_resistance(9 , 0.03)

print("RESISTANCE = ",results ,"ohms")
print(calc_resistance.__doc__)

# Exercise 1 : Power test
power_results= calc_power(24 , 2)
print("POWER = ",power_results ,"Watts")

assert calc_power(24 , 2) == 288
assert calc_power(12 , 4) == 36
assert calc_power(10 , 2) == 50


print(calc_power.__doc__)
