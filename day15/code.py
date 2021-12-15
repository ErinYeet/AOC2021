f = open("input.txt", "r")
lines = f.readlines()
lines = [line.rstrip() for line in lines]

numbergrid = []

for line in lines:
    numbergrid.append([int(i) for i in line])

pathgrid = [[0]*len(numbergrid[0]) for _ in range(len(numbergrid))]
pathgrid[0][0] = numbergrid[0][0]

boundary = []
current = [0,0]

#part1

while True:
    # compute surrounding points
    if current[0] < len(pathgrid)-1:
        if pathgrid[current[0]+1][current[1]] == 0:
            pathgrid[current[0]+1][current[1]] = pathgrid[current[0]][current[1]] + numbergrid[current[0]+1][current[1]] 
            boundary.append([current[0]+1,current[1]])
            
    if current[1] < len(pathgrid[0])-1:
        if pathgrid[current[0]][current[1]+1] == 0:
            pathgrid[current[0]][current[1]+1] = pathgrid[current[0]][current[1]] + numbergrid[current[0]][current[1]+1] 
            boundary.append([current[0],current[1]+1])
            
    if current[0] > 0:
        if pathgrid[current[0]-1][current[1]] == 0:
            pathgrid[current[0]-1][current[1]] = pathgrid[current[0]][current[1]] + numbergrid[current[0]-1][current[1]] 
            boundary.append([current[0]-1,current[1]])
            
    if current[1] > 0:
        if pathgrid[current[0]][current[1]-1] == 0:
            pathgrid[current[0]][current[1]-1] = pathgrid[current[0]][current[1]] + numbergrid[current[0]][current[1]-1] 
            boundary.append([current[0],current[1]-1])

    #get the lowest boundary point     
    if boundary == []:
        break
    lowest_val = 99999999
    lowest_index = 0
    for i in range(len(boundary)):
        if pathgrid[boundary[i][0]][boundary[i][1]] < lowest_val:
            lowest_val = pathgrid[boundary[i][0]][boundary[i][1]]
            lowest_index = i
    current = boundary.pop(lowest_index)
print(pathgrid[-1][-1] - pathgrid[0][0])

#part2
bignumbergrid = [[0]*(len(numbergrid[0])*5) for _ in range(len(numbergrid)*5)]
bigpathgrid = [[0]*len(bignumbergrid[0]) for _ in range(len(bignumbergrid))]
bigpathgrid[0][0] = numbergrid[0][0]


#setup big grid
for x in range(len(bignumbergrid)):
    for y in range(len(bignumbergrid[x])):
        bignumbergrid[x][y] = (numbergrid[x%len(numbergrid)][y%len(numbergrid[0])] + x//len(numbergrid) + y//len(numbergrid[0]))
        if bignumbergrid[x][y] % 9 == 0:
            bignumbergrid[x][y] = 9
        else:
            bignumbergrid[x][y] = bignumbergrid[x][y] % 9
            
#same method as part 1, duplicated code is bad but I am lazy
boundary = []
current = [0,0]

while True:
    # compute surrounding points
    if current[0] < len(bigpathgrid)-1:
        if bigpathgrid[current[0]+1][current[1]] == 0:
            bigpathgrid[current[0]+1][current[1]] = bigpathgrid[current[0]][current[1]] + bignumbergrid[current[0]+1][current[1]] 
            boundary.append([current[0]+1,current[1]])
            
    if current[1] < len(bigpathgrid[0])-1:
        if bigpathgrid[current[0]][current[1]+1] == 0:
            bigpathgrid[current[0]][current[1]+1] = bigpathgrid[current[0]][current[1]] + bignumbergrid[current[0]][current[1]+1] 
            boundary.append([current[0],current[1]+1])
            
    if current[0] > 0:
        if bigpathgrid[current[0]-1][current[1]] == 0:
            bigpathgrid[current[0]-1][current[1]] = bigpathgrid[current[0]][current[1]] + bignumbergrid[current[0]-1][current[1]] 
            boundary.append([current[0]-1,current[1]])
            
    if current[1] > 0:
        if bigpathgrid[current[0]][current[1]-1] == 0:
            bigpathgrid[current[0]][current[1]-1] = bigpathgrid[current[0]][current[1]] + bignumbergrid[current[0]][current[1]-1] 
            boundary.append([current[0],current[1]-1])
         
    if boundary == []:
        break

    #get the lowest boundary point
    lowest_val = 99999999
    lowest_index = 0
    for i in range(len(boundary)):
        if bigpathgrid[boundary[i][0]][boundary[i][1]] < lowest_val:
            lowest_val = bigpathgrid[boundary[i][0]][boundary[i][1]]
            lowest_index = i
    current = boundary.pop(lowest_index)
print(bigpathgrid[-1][-1] - bigpathgrid[0][0])
