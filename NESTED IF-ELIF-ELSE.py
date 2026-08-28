voltage = float(input("enter batter voltage"))
if voltage > 12.5:
    print("GOOD")
elif voltage >= 11.5:
    print("MARGINAL")
else:
    print("LOW")

