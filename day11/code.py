f = open("input.txt", "r")
lines = f.readlines()
lines = [line.rstrip() for line in lines]

gamegrid = []
for x in lines:
    gamegrid.append([int(y) for y in x])

flashtotal = 0

#part 1
for t in range(100):
    # add one
    for x in range(10):
        for y in range(10):
            gamegrid[x][y] = gamegrid[x][y] + 1
    
    flashgrid = [[False]*10 for _ in range(10)]
    # flahses happen
    while True:
        newflash = False
        for x in range(10):
            for y in range(10):
                if gamegrid[x][y] < 10:
                    continue
                elif flashgrid[x][y]:
                    continue
                
                flashgrid[x][y] = True
                flashtotal = flashtotal+1
                newflash = True
                
                validneighbors = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
                if x == 0:
                    validneighbors = [ a for a in validneighbors if a not in [[-1,-1],[-1,0],[-1,1]]]
                if x == 9:
                    validneighbors = [ a for a in validneighbors if a not in [[1,-1],[1,0],[1,1]]]
                if y == 0:
                    validneighbors = [ a for a in validneighbors if a not in [[1,-1],[0,-1],[-1,-1]]]
                if y == 9:
                    validneighbors = [ a for a in validneighbors if a not in [[1,1],[0,1],[-1,1]]]
                for i,j in validneighbors:
                    gamegrid[x+i][y+j] = gamegrid[x+i][y+j] + 1
        if not newflash:
            break
                                
    #reset flashy
    for x in range(10):
        for y in range(10):
            if flashgrid[x][y]:
                gamegrid[x][y] = 0

print(flashtotal)

gamegrid = []
for x in lines:
    gamegrid.append([int(y) for y in x])

#part 2
step = 0
while True:
    step = step + 1
    # add one
    for x in range(10):
        for y in range(10):
            gamegrid[x][y] = gamegrid[x][y] + 1
    
    flashgrid = [[False]*10 for _ in range(10)]
    # flahses happen
    while True:
        newflash = False
        for x in range(10):
            for y in range(10):
                if gamegrid[x][y] < 10:
                    continue
                elif flashgrid[x][y]:
                    continue
                
                flashgrid[x][y] = True
                newflash = True
                
                validneighbors = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
                if x == 0:
                    validneighbors = [ a for a in validneighbors if a not in [[-1,-1],[-1,0],[-1,1]]]
                if x == 9:
                    validneighbors = [ a for a in validneighbors if a not in [[1,-1],[1,0],[1,1]]]
                if y == 0:
                    validneighbors = [ a for a in validneighbors if a not in [[1,-1],[0,-1],[-1,-1]]]
                if y == 9:
                    validneighbors = [ a for a in validneighbors if a not in [[1,1],[0,1],[-1,1]]]
                for i,j in validneighbors:
                    gamegrid[x+i][y+j] = gamegrid[x+i][y+j] + 1
        if not newflash:
            break
                                
    #reset flashy

    allflashed = True
        
    for x in range(10):
        for y in range(10):
            if flashgrid[x][y]:
                gamegrid[x][y] = 0
            else:
                allflashed = False
    if allflashed:
        break
print(step)
