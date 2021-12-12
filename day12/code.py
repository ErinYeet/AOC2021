from collections import defaultdict

f = open("input.txt", "r")
lines = f.readlines()
lines = [line.rstrip() for line in lines]

connections = defaultdict(list)

for line in lines:
    connections[line.split("-")[0]].append(line.split("-")[1])
    connections[line.split("-")[1]].append(line.split("-")[0])

print(connections)

#part1
finalpaths = []
wippaths = [["start"]]
while len(wippaths) > 0:
    currentpath = wippaths.pop()
    for nextstep in connections[currentpath[-1]]:
        nextpath = currentpath.copy()
        if nextstep == "end":
            nextpath.append(nextstep) 
            finalpaths.append(nextpath)
        elif nextstep == "start":
            continue
        elif nextstep.isupper():
            nextpath.append(nextstep) 
            wippaths.append(nextpath)
        elif nextstep not in currentpath:
            nextpath.append(nextstep) 
            wippaths.append(nextpath)
print(finalpaths)
print(len(finalpaths))

#part2
finalpaths = []
wippaths = [["start"]]
revisit_alloweds = [[True]]
while len(wippaths) > 0:
    currentpath = wippaths.pop()
    revisit = revisit_alloweds.pop()
    for nextstep in connections[currentpath[-1]]:
        nextpath = currentpath.copy()
        if nextstep == "end":
            nextpath.append(nextstep) 
            finalpaths.append(nextpath)
        elif nextstep == "start":
            continue
        elif nextstep.isupper():
            nextpath.append(nextstep) 
            wippaths.append(nextpath)
            revisit_alloweds.append(revisit)
        elif nextstep not in currentpath:
            nextpath.append(nextstep) 
            wippaths.append(nextpath)
            revisit_alloweds.append(revisit)
        elif revisit:
            nextpath.append(nextstep) 
            wippaths.append(nextpath)
            revisit_alloweds.append(False)
print(finalpaths)
print(len(finalpaths))
