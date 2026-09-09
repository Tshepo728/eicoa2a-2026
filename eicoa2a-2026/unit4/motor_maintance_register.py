Above_85 = 0
motors = {
    "M-101": {
        "location": "Workshop A",
        "rated_power": 5.5,
        "temperature": 72,
        "status": "RUNNING",
        "faults": ["F01", "F02"]
    },
    "M-102": {
        "location": "Workshop B",
        "rated_power": 7.5,
        "temperature": 88,
        "status": "RUNNING",
        "faults": ["F02","F03"]
    },
    "M-103": {
        "location": "Pump Station",
        "rated_power": 11,
        "temperature": 79,
        "status": "service required",
        "faults":["F01","F04"]
    }
}
print("motor maintanance register")
print(motors["M-102"])
motors["M-102"]["status"] = "overheat"
print(motors["M-102"])
for motor_id,motor in motors.items():
    print(motor_id,motor["location"],
          motor["rated_power"],
          motor["temperature"],
          motor["status"],
          motor["faults"]
    )
    
    if motor["temperature"] > 85:
        Above_85 += 1
    print("motors above 85 degree celsius are :",Above_85)
    







    
          

      


