f = open("input.txt", "r")
lines = f.readlines()
lines = [line.rstrip() for line in lines]

fish = [int(x) for x in lines[0].split(",")]
#fish =[3,4,3,1,2]

#part1
for t in range(80):
    fishcount = len(fish)
    for x in range(fishcount):
        if fish[x] == 0:
            fish[x] = 6
            fish.append(8)
        else:
            fish[x] = fish[x] - 1
print(len(fish))


fish = [int(x) for x in lines[0].split(",")]
#fish =[3,4,3,1,2]

#part2
fishagelist = [0,0,0,0,0,0,0,0,0]

for x in fish:
    fishagelist[x] = fishagelist[x]+1

for t in range(256):
    newagelist = [0,0,0,0,0,0,0,0,0]
    for x in range(8):
        if x != 9:
            newagelist[x] = fishagelist[x+1]
    newagelist[8] = fishagelist[0]
    newagelist[6] = newagelist[6] + fishagelist[0]
    fishagelist = newagelist.copy()
print(sum(fishagelist))
