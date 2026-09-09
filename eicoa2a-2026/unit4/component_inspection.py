import random
from tabulate import tabulate

component = { "ECU-101": 4.96,
               "ECU-102": 5.08,
               "ECU-103": 4.88,
               "ECU-104": 5.02, 
               "ECU-105": 5.15,
               "ECU-106": 4.99, 
               "ECU-107": 4.91, 
               "ECU-108": 5.05 
}

voltage_tolerance = (4.9 ,5.10)

random.seed(42)
selected_ids = random.sample(list(component.keys()),4)
minimum_voltage ,maximum_voltage = voltage_tolerance
inspection_rows = []
failed_components = set()

PASS = 0
FAIL = 0
for component_id in selected_ids:
    voltage = component[component_id]
    if minimum_voltage < voltage < maximum_voltage:
        PASS += 1
        inspection_rows.append([component_id, voltage, "Pass"])
    else:
        FAIL += 1
        inspection_rows.append([component_id, voltage, "Fail"])

print("\nComponent Inspection Results")
print(tabulate(inspection_rows,headers=["Component ID",
                                         "Voltage (V)", "Result"],
        tablefmt="grid")
)

