#part2

f = open("input.txt", "r")
lines = f.readlines()
lines = [line.rstrip() for line in lines]

boards = []
boardwins = []
numbers = [int(a) for a in lines[0].split(",")]

print(numbers)

x = 1

while True:
    if lines[x] == "":
        board = []
        winsboard = []
        for y in range(5):
            x = x+1
            thisline = lines[x]
            thisnums = []
            for z in range(5):
                thisnums.append(int(thisline[0+z*3:2+z*3]))
            board.append(thisnums)
            winsboard.append([0]*5)
        boards.append(board)
        boardwins.append(winsboard)
        x=x+1
        if x >= len(lines):
            break

boardshavewon = [False] * len(boards)

for number in numbers:
    for x in range(len(boards)):
        for y in range(5):
            for z in range(5):
                if number == boards[x][y][z]:
                    boardwins[x][y][z] = 1
    winningboard = 0
    for x in range(len(boards)):
        haswon = False
        for y in range(5):
            if sum(boardwins[x][y])==5:
                haswon = True
                if not boardshavewon[x]:
                    winningboard = x
        for z in range(5):
            total = 0
            for t in range(5):
                total = total + boardwins[x][t][z]
            if total == 5:
                haswon = True
                if not boardshavewon[x]:
                    winningboard = x
        
        if haswon:
            boardshavewon[x] = True
    allwon = True
    for value in boardshavewon:
        if not value:
            allwon = False
    if allwon:
        print("yeah")
        print(number)
        score = 0
        for y in range(5):
            for z in range(5):
                if boardwins[winningboard][y][z] == 0:
                    score = score + boards[winningboard][y][z]
        print(score*number)
        break
