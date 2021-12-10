f = open("input.txt", "r")
lines = f.readlines()
lines = [line.rstrip() for line in lines]

inputs = [a.split("|")[0].split(" ")[:-1] for a in lines]
outputs = [a.split("|")[1].split(" ")[1:] for a in lines]

lentovalue = {2: 1,
              4: 4,
              3: 7,
              7: 8,
}
#part1
counter = 0

for nums in outputs:
    for num in nums:
        if len(num) in [2,4,3,7]:
            counter = counter + 1

print(counter)

#part2

total = 0

for x in range(len(inputs)):
    sortedinputs = [''.join(sorted(a)) for a in inputs[x]]
    sortedoutputs = [''.join(sorted(a)) for a in outputs[x]]
    #print(sortedinputs)
    #print(sortedoutputs)
    results = {}
    invresults = {}

    #this whole thing can probably be more efficient but this is how my brain works
    
    # do the easy ones 1,4,7,8
    for value in sortedinputs:
        if len(value) in [2,4,3,7]:
            results[value] = lentovalue[len(value)]
            invresults[lentovalue[len(value)]] = value
    # do the rest
    for value in sortedinputs:
        # do 9,6,0
        if len(value) == 6:
            if set(invresults[4]).issubset(set(value)):
                results[value] = 9
                invresults[9] = value
            elif set(invresults[1]).issubset(set(value)):
                results[value] = 0
                invresults[0] = value
            else:
                results[value] = 6
                invresults[6] = value
        #2,3,5
        if len(value) == 5:
            if set(invresults[1]).issubset(set(value)):
                results[value] = 3
                invresults[3] = value
            elif len(set(invresults[4]).intersection(set(value))) == 2:
                results[value] = 2
                invresults[2] = value
            else:
                results[value] = 5
                invresults[5] = value
                
    total = total + (results[sortedoutputs[0]] * 1000)
    total = total + (results[sortedoutputs[1]] * 100)
    total = total + (results[sortedoutputs[2]] * 10)
    total = total + (results[sortedoutputs[3]] * 1)
print(total)
