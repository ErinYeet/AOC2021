f = open("input.txt", "r")
lines = f.readlines()
lines = [line.rstrip() for line in lines]

starts = [[int(line.split(" ")[0].split(",")[0]),int(line.split(" ")[0].split(",")[1])] for line in lines]
ends = [[int(line.split(" ")[2].split(",")[0]),int(line.split(" ")[2].split(",")[1])] for line in lines]

print(starts)
print(ends)

xsize = 0
ysize = 0

for x,y in starts:
    if x > xsize:
        xsize = x
    if y > ysize:
        ysize = y
for x,y in ends:
    if x > xsize:
        xsize = x
    if y > ysize:
        ysize = y

ysize = ysize + 1
xsize = xsize + 1

grid = [[0] * ysize for _ in range(xsize)]

#part1
for t in range(len(starts)):
    x,y = starts[t]
    endx,endy = ends[t]
    #print(x,y)
    if (x != endx) and (y != endy):
        continue
    if x == endx:
        xchange = 0
    elif x >= endx:
        xchange = -1
    else:
        xchange = 1
    if y == endy:
        ychange = 0
    elif y >= endy:
        ychange = -1
    else:
        ychange = 1
    while True:
        grid[x][y] = grid[x][y] + 1
        if x == endx and y == endy:
            break
        x = x + xchange
        y = y + ychange

#print(grid)

anscount = 0

for x in range(xsize):
    for y in range(ysize):
        if grid[x][y] >= 2:
            anscount = anscount+1
print(anscount)

# part2

grid = [[0] * ysize for _ in range(xsize)]

for t in range(len(starts)):
    x,y = starts[t]
    endx,endy = ends[t]
    #print(x,y)
    if x == endx:
        xchange = 0
    elif x >= endx:
        xchange = -1
    else:
        xchange = 1
    if y == endy:
        ychange = 0
    elif y >= endy:
        ychange = -1
    else:
        ychange = 1

    while True:
        grid[x][y] = grid[x][y] + 1
        if x == endx and y == endy:
            break
        x = x + xchange
        y = y + ychange

#print(grid)

anscount = 0

for x in range(xsize):
    for y in range(ysize):
        if grid[x][y] >= 2:
            anscount = anscount+1
print(anscount)
