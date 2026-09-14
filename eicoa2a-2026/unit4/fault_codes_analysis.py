reported_faults = ["F01", "F03", "F01", "F07", "F03", "F12", "F07"]
print(reported_faults)
def unique_faults(reported_faults):
    return set(reported_faults)
unique_faults = unique_faults(reported_faults)
print(unique_faults)
print("number of unique faults :", len(unique_faults))

Area_A_faults = {"f01","F03", "F07", "F12"}
Area_B_faults = {"F03","F07"}
common_faults = Area_A_faults & Area_B_faults
Area_A_faults_only = Area_A_faults - Area_B_faults
print("common faults :", common_faults)
print("faults in area a :", Area_A_faults_only)