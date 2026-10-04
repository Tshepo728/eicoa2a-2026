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
    average = count / total
    with open("summary.txt", "w") as file:
        file.write(f"Total weight: {total}\n")
        file.write(f"valid entries: {count}\n")
        file.write(f"Average weight: {average:.2f}\n")
except FileNotFoundError:
    print("weight data is missing...")
