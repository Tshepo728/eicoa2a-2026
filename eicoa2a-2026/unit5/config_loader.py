def load_config(filename):
    try:
        with open("filename", "r") as file:
            lines = file.readlines()

            mode = lines[0].strip()
            timeout = int(lines[1].srtip())

        return mode , timeout

    except FileNotFoundError:
        print(f"WARNING :{filename} not found using default settings")
        return "DEFAULT", 30

mode ,timeout =load_config("config.txt")
print(f"Active mode: {mode}")
print(f"timeout :{timeout}s")



