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
minimum__voltage ,maximum_voltage = voltage_tolerance
inspection_rows = []
failed_components = set()



