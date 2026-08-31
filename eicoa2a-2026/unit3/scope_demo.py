safety_margin = 1.5
def apply_local_threshold(value):
    safety_margin = 2.50
    results = value * safety_margin
    return results

if __name__=="__main__":
    value = float(input("enter value: "))
    results = apply_local_threshold(value)
    print(f"local safety margin = {results :.2f} ")
    print(f"global safety margin = {safety_margin :.2f} ")