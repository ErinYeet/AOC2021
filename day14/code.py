from collections import Counter
from collections import defaultdict

f = open("input.txt", "r")
lines = f.readlines()
lines = [line.rstrip() for line in lines]

polymer_str = lines[0]
pair_rules = {}
polymer = defaultdict(int)


for x in range(len(polymer_str)-1):
    polymer[polymer_str[x:x+2]] = polymer[polymer_str[x:x+2]] + 1

print(polymer)

for x in range(2,len(lines)):
    pair_rules[lines[x][0:2]] = [lines[x][0]+lines[x][-1],lines[x][-1]+lines[x][1]]

print(pair_rules)

#p1/p2 change this
for i in range(40):
    newpoly = defaultdict(int)
    print(i)
    for k in polymer:
        newpoly[pair_rules[k][0]] = newpoly[pair_rules[k][0]] + polymer[k]
        newpoly[pair_rules[k][1]] = newpoly[pair_rules[k][1]] + polymer[k]
    polymer = newpoly

countdict = defaultdict(int)

for k in polymer:
    countdict[k[0]] = countdict[k[0]] + polymer[k]
    countdict[k[1]] = countdict[k[1]] + polymer[k]

countdict[polymer_str[0]] = countdict[polymer_str[0]] + 1
countdict[polymer_str[-1]] = countdict[polymer_str[-1]] + 1
print(countdict)
results = list(countdict.values())
results.sort()
print((results[-1] - results[0])/2)
