

f = open("input.txt", "r")
lines = f.readlines()
lines = [line.rstrip() for line in lines]

intlines = [int(line) for line in lines]
silvercount = 0

for x in range(1,len(intlines)):
    if intlines[x] > intlines[x-1]:
        silvercount = silvercount+1

print(silvercount)

goldcount = 0

rollingsums = [sum(intlines[x:x+3]) for x in range(len(intlines)-2)]

for x in range(1,len(rollingsums)):
    if rollingsums[x] > rollingsums[x-1]:
        goldcount = goldcount+1

print(goldcount)
