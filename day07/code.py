f = open("input.txt", "r")
lines = f.readlines()
lines = [line.rstrip() for line in lines]

data = [int(a) for a in lines[0].split(",")]
submax = 0
for sub in data:
    if sub > submax:
        submax = sub
#p1
fuelmin = 0
for x in range(0,submax):
    fuel = 0
    for sub in data:
        fuel = fuel + abs(sub-x)
    if x == 0:
        fuelmin = fuel
    elif fuelmin > fuel:
        fuelmin = fuel
print(fuelmin)

#p2
fuelmin = 0
for x in range(0,submax):
    fuel = 0
    for sub in data:
        diff = abs(sub-x)
        fuel = fuel + int(0.5*diff*(diff+1))
    if x == 0:
        fuelmin = fuel
    elif fuelmin > fuel:
        fuelmin = fuel
print(fuelmin)
