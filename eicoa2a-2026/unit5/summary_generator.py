print("starting weight summary...")

total = 0
count = 0

with open("weights.txt", "r") as file:
    for line in file:
        cleaned_line = line.strip()
        print(cleaned_line)