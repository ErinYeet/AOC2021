
f = open("input.txt", "r")
lines = f.readlines()
lines = [line.rstrip() for line in lines]

heightmap = []

for line in lines:
    heightmap.append([int(a) for a in line])


#part 1
risksum = 0
riskypoints = []
for x in range(len(heightmap)):
    for y in range(len(heightmap[x])):
        validneighbors = []
        risky = True
        if x != 0:
            validneighbors.append([x-1,y])
        if x != len(heightmap) - 1:
            validneighbors.append([x+1,y])
        if y != 0:
            validneighbors.append([x,y-1])
        if y != len(heightmap[x]) - 1:
            validneighbors.append([x,y+1])
        for a,b in validneighbors:
            if heightmap[a][b] <= heightmap[x][y]:
                risky = False
        if risky:
            risksum = risksum + heightmap[x][y] + 1
            riskypoints.append([x,y])
print(risksum)

#part2
baisins = []
baisinpoints = []

for x,y in riskypoints:
    if [x,y] in baisinpoints or heightmap[x][y] == 9:
        continue
    currentbaisin = [[x,y]]
    currentedge = [[x,y]]
    while True:
        nextedge = []
        validneighbors = []
        for i,j in currentedge:
            if i != 0:
                validneighbors.append([i-1,j])
            if i != len(heightmap) - 1:
                validneighbors.append([i+1,j])
            if j != 0:
                validneighbors.append([i,j-1])
            if j != len(heightmap[i]) - 1:
                validneighbors.append([i,j+1])
            for a,b in validneighbors:
                if [a,b] not in currentbaisin and [a,b] not in currentedge and [a,b] not in nextedge and heightmap[a][b] != 9:
                    baisinpoints.append([a,b])
                    nextedge.append([a,b])
        if nextedge == []:
            break
        else:
            #print(currentbaisin)
            currentedge = nextedge.copy()
            currentbaisin.extend(nextedge.copy())
    baisins.append(currentbaisin)
print(baisins)

prod = 1

baisinlens = [len(baisin) for baisin in baisins]
baisinlens.sort(reverse=True)

for x in range(3):
    prod = prod * baisinlens[x]
print(prod)
