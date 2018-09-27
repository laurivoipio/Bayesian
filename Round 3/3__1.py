
with open("windshieldy1.txt") as input_file:
    for line in input_file:
        line = line.strip()
        for number in line.split():
            float(number)
data = open("windshieldy1.txt", "r")
data_as_list = data.read().split("\n")

print(data_as_list)