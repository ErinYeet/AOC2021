

f = open("input.txt", "r")
lines = f.readlines()
lines = [line.rstrip() for line in lines]

x = 0
y = 0

for line in lines:
    command = line.split(" ")[0]
    distance = int(line.split(" ")[1])
    if command == "forward":
        x = x + distance
    if command == "down":
        y = y + distance
    if command == "up":
        y = y - distance

print(x*y)

x = 0
y = 0

aim = 0

for line in lines:
    command = line.split(" ")[0]
    distance = int(line.split(" ")[1])
    if command == "forward":
        x = x + distance
        y = y + (distance*aim)
    if command == "down":
        aim = aim + distance
    if command == "up":
        aim = aim - distance

print(x*y)
