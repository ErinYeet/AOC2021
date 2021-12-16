f = open("input.txt", "r")
lines = f.readlines()
lines = [line.rstrip() for line in lines]

#hex to binary

binarychart = {'0' : "0000",
               '1' : "0001",
               '2' : "0010",
               '3' : "0011",
               '4' : "0100",
               '5' : "0101",
               '6' : "0110",
               '7' : "0111",
               '8' : "1000",
               '9' : "1001",
               'A' : "1010",
               'B' : "1011",
               'C' : "1100",
               'D' : "1101",
               'E' : "1110",
               'F' : "1111",
}

binaryin = []

for line in lines:
    for char in line:
       binaryin.extend(list(binarychart[char]))

# parsing

# list of dictionaries
# packets can have
# version
# type_id
# value
# sub_packets (list of ints that are keys)
# parent_packet (int that is a key)
# length_type_id
# length_value
# length_processed
packet_heira = []

i = 0

while i < len(binaryin):
    starti = i
    #get type and version
    version = int("".join(binaryin[i:i+3]),2)
    i = i+3
    type_id = int("".join(binaryin[i:i+3]),2)
    i = i+3
    #get value if it is a literal
    if type_id == 4:
        valuebinary = []
        while True:
            if binaryin[i] == '0':
                stopping = True
            else:
                stopping = False
            i = i+1
            valuebinary.extend("".join(binaryin[i:i+4]))
            i = i+4
            if stopping:
                break
        value = int("".join(valuebinary),2)
    #get sub packet info if it is an operator
    else:
        length_type_id = int(binaryin[i])
        i = i+1
        if length_type_id == 0:
            length_value = int("".join(binaryin[i:i+15]),2)
            i = i+15
        if length_type_id == 1:
            length_value = int("".join(binaryin[i:i+11]),2)
            i = i+11
            
    j = len(packet_heira)
    parent_id = None
    parents = []
    # find and update parents
    if j != 0:
        # find first parent
        for x in reversed(range(j)):
            if packet_heira[x]["type_id"] != 4:
                if packet_heira[x]["length_value"] > packet_heira[x]["length_processed"]:
                    parent_id = x
                    break
        # find other ancestors
        parent_search = [parent_id]
        while len(parent_search) > 0:
            current_id = parent_search.pop()
            if current_id is None:
                continue
            parents.append(current_id)
            parent_search.append(packet_heira[current_id]["parent_packet"])
        # update them with what we processed
        for x in parents:
            if packet_heira[x]["length_type_id"] == 0:
                packet_heira[x]["length_processed"] = packet_heira[x]["length_processed"] + (i - starti)
            if packet_heira[x]["length_type_id"] == 1 and x == parent_id:
                packet_heira[x]["length_processed"] = packet_heira[x]["length_processed"] + 1
        # make the packet dictionary
        if type_id == 4:
            thispacket = { "version" : version,
                           "type_id" : type_id,
                           "value" : value,
                           "parent_packet" : parent_id,
                           }
        else:
            thispacket = { "version" : version,
                           "type_id" : type_id,
                           "parent_packet" : parent_id,
                           "sub_packets" : [],
                           "length_type_id" : length_type_id,
                           "length_value" : length_value,
                           "length_processed" : 0,
                           }
        # add this packet
        packet_heira.append(thispacket)
        # update parent
        packet_heira[parent_id]["sub_packets"].append(j)
    else:
        # make the dict
        thispacket = { "version" : version,
                       "type_id" : type_id,
                       "parent_packet" : None,
                       "sub_packets" : [],
                       "length_type_id" : length_type_id,
                       "length_value" : length_value,
                       "length_processed" : 0,
                       }
        # add this packet
        packet_heira.append(thispacket)
    #check if every packet is full
    finished = True
    for x in range(j+1):
        if packet_heira[x]["type_id"] != 4:
            if packet_heira[x]["length_value"] > packet_heira[x]["length_processed"]:
                finished=False
    if finished:
        break

#part 1
versionsum = 0
for packet in packet_heira:
    versionsum = versionsum + packet["version"]    
print(versionsum)

#part 2
#go through the packets
#if it is an instruction set value to the result
instructions = [0]
while len(instructions) > 0:
    current = instructions[-1]

    #check if all sub packets have values
    #if not add them to instructions to be calculated
    cando = True
    for sub in packet_heira[current]["sub_packets"]:
        if "value" not in packet_heira[sub]:
            cando = False
            instructions.append(sub)
    #process instruction and save result as value
    if cando:
        #sum
        if packet_heira[current]["type_id"] == 0:
            value = 0
            for sub in packet_heira[current]["sub_packets"]:
                value = value + packet_heira[sub]["value"]
        #product
        elif packet_heira[current]["type_id"] == 1:
            value = 1
            for sub in packet_heira[current]["sub_packets"]:
                value = value * packet_heira[sub]["value"]
        #minimum
        elif packet_heira[current]["type_id"] == 2:
            value = packet_heira[packet_heira[current]["sub_packets"][0]]["value"]
            for sub in packet_heira[current]["sub_packets"]:
                value = min(value,packet_heira[sub]["value"])
        #maximum
        elif packet_heira[current]["type_id"] == 3:
            value = packet_heira[packet_heira[current]["sub_packets"][0]]["value"]
            for sub in packet_heira[current]["sub_packets"]:
                value = max(value,packet_heira[sub]["value"])
        #greater than
        elif packet_heira[current]["type_id"] == 5:
            if packet_heira[packet_heira[current]["sub_packets"][0]]["value"] > packet_heira[packet_heira[current]["sub_packets"][1]]["value"]:
                value = 1
            else:
                value = 0
        #less than
        elif packet_heira[current]["type_id"] == 6:
            if packet_heira[packet_heira[current]["sub_packets"][0]]["value"] < packet_heira[packet_heira[current]["sub_packets"][1]]["value"]:
                value = 1
            else:
                value = 0
        #equals
        elif packet_heira[current]["type_id"] == 7:
            if packet_heira[packet_heira[current]["sub_packets"][0]]["value"] == packet_heira[packet_heira[current]["sub_packets"][1]]["value"]:
                value = 1
            else:
                value = 0
        packet_heira[current]["value"] = value
        instructions.pop()

print(packet_heira[0]["value"])
