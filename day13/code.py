import itertools

f = open("input.txt", "r")
lines = f.readlines()
lines = [line.rstrip() for line in lines]

dots = []
folds = []

#setup data

for line in lines:
    if line == "":
        continue
    if line[0] == "f":
        axis = line.split("=")[0][-1]
        num = int(line.split("=")[1])
        folds.append([axis,num])
    else:
        x = int(line.split(",")[0])
        y = int(line.split(",")[1])
        dots.append([x,y])

#part1
newdots = []
axis = folds[0][0]
num = folds[0][1]
for dot in dots:
    if axis == "x":
        if dot[0] < num:
            newdots.append(dot.copy())
        else:
            newdots.append([((2*num) - dot[0]),dot[1]])
    if axis == "y":
        if dot[1] < num:
            newdots.append(dot.copy())
        else:
            newdots.append([dot[0],((2*num) - dot[1])])
    #cant use the list set trick to remove duplicate in list of lists
    newdots.sort()
    newdots = list(k for k,_ in itertools.groupby(newdots))
print(len(newdots))

#part2

#foldit
for fold in folds:
    newdots = []
    axis = fold[0]
    num = fold[1]
    for dot in dots:
        if axis == "x":
            if dot[0] < num:
                newdots.append(dot.copy())
            else:
                newdots.append([((2*num) - dot[0]),dot[1]])
        if axis == "y":
            if dot[1] < num:
                newdots.append(dot.copy())
            else:
                newdots.append([dot[0],((2*num) - dot[1])])
        #cant use the list set trick to remove duplicate in list of lists
        newdots.sort()
        newdots = list(k for k,_ in itertools.groupby(newdots))
    dots = newdots.copy()

#printit
xmax = 0
ymax = 0
for dot in dots:
    if dot[0] > xmax:
        xmax = dot[0]
    if dot[1] > ymax:
        ymax = dot[1]
for y in range(ymax+1):
    for x in range(xmax+1):
        if [x,y] in dots:
            print("#",end='')
        else:
            print(".",end='')
    print()
