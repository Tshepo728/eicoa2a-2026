print("starting weight summary...")

total = 0
count = 0
try:
    with open("weights.txt", "r") as file:
        for line in file:
            cleaned_line = line.strip()
            print(cleaned_line)
            
            try:
                weight = float(cleaned_line)
                total += weight
                count += 1
            except ValueError:
                continue
except FileNotFoundError:
    print("weights.txt file not found...")
