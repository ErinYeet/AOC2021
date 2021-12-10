
f = open("input.txt", "r")
lines = f.readlines()
lines = [line.rstrip() for line in lines]

listlines = [list(line) for line in lines]

#both parts at once, gasp

part1_score = 0
part2_scores = []

#guess this could have been done for part 1 too huh
part2_scoredict = { '(' : 1,
                    '[' : 2,
                    '{' : 3,
                    '<' : 4
}

for line in listlines:
    index = 0
    broke = False
    while index < len(line):
        if line[index] in ['(','[','{','<']:
            index = index + 1
            continue
        else:
            # realied how this could be neater after I had already done it
            if line[index] == ')':
                if line[index] == 0 or line[index-1] != '(':
                    part1_score = part1_score + 3
                    broke = True
                    break
            if line[index] == ']':
                if line[index] == 0 or line[index-1] != '[':
                    part1_score = part1_score + 57
                    broke = True
                    break
            if line[index] == '}':
                if line[index] == 0 or line[index-1] != '{':
                    part1_score = part1_score + 1197
                    broke = True
                    break
            if line[index] == '>':
                if line[index] == 0 or line[index-1] != '<':
                    part1_score = part1_score + 25137
                    broke = True
                    break

            line.pop(index)
            line.pop(index-1)
            index = index - 1
            
    if not broke:
        line.reverse()
        linescore = 0
        for x in line:
            linescore = (linescore * 5) + part2_scoredict[x]
        part2_scores.append(linescore)
print(part1_score)
part2_scores.sort()
key = int(len(part2_scores)/2)
print(part2_scores[key])
