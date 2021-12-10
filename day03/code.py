f = open("input.txt", "r")
lines = f.readlines()
lines = [line.rstrip() for line in lines]

positionsums = [0] * len(lines[0])
midpoint = len(lines)/2

for line in lines:
    for x in range(len(line)):
        positionsums[x] = positionsums[x] + int(line[x])

print(positionsums)
print(midpoint)

gammastr = ""
epsilonstr = ""

for pos in positionsums:
    if pos > midpoint:
        gammastr = gammastr + "1"
        epsilonstr = epsilonstr + "0"
    else:
        gammastr = gammastr + "0"
        epsilonstr = epsilonstr + "1"

gamma = int(gammastr,2)
epsilon = int(epsilonstr,2)

print(gamma*epsilon)

oxygenresult = lines.copy()
carbonresult = lines.copy()

for x in range(len(lines[0])):
    if len(oxygenresult)>1:
        oxycount = 0
        for oxyline in oxygenresult:
            if oxyline[x] == "1":
                oxycount = oxycount + 1
        oxymid = len(oxygenresult) / 2
        if oxycount >= oxymid:
            oxytarget = "1"
        else:
            oxytarget = "0"
        oxygenresult = [a for a in oxygenresult if a[x] == oxytarget]
    if len(carbonresult)>1:
        carboncount = 0
        for carbonline in carbonresult:
            if carbonline[x] == "1":
                carboncount = carboncount + 1
        carbonmid = len(carbonresult) / 2
        if carboncount >= carbonmid:
            carbontarget = "0"
        else:
            carbontarget = "1"
        carbonresult = [a for a in carbonresult if a[x] == carbontarget]

oxynum = int(oxygenresult[0],2)
carbonnum = int(carbonresult[0],2)

print(oxygenresult,carbonresult)

print(oxynum*carbonnum)
