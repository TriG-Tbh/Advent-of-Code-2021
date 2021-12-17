import helper
with open(helper.nrml("day16.txt")) as f:
    contents = f.read()

mapped = {'0': "0000", '1': "0001", '2': "0010", '3': "0011", '4': "0100", '5': "0101", '6': "0110", '7': "0111", '8': "1000", '9': "1001",  'A': "1010", 'B': "1011", 'C': "1100", 'D': "1101", 'E': "1110", 'F': "1111"}



def convert(fromstr):
    new = ""
    for item in fromstr:
        new += mapped[item]
    return new
versions = []

new = convert(contents)
with open(helper.nrml("total.txt"), 'w') as f:
    f.write(new)

def operator(new, I, ignore=False):
    if I == "0":
        #print(new[7:22])
        L = int(new[7:22], 2)
        if not ignore:
            new = new[:-2]
        container = new[22:(22+L)]
        while len(container) > 0:
            container = parse(container, ignore=True)
        new = new[(22+L):]
    else:
        L = int(new[7:18])
        if ignore:
            new = new[18:]
        else:
            new = new[18:-2]
        for _ in range(L):
            new = parse(new, ignore=True)
    return new

def value(new, ignore=False):
    index = 6
    while new[index] == "1":
        value = new[index:index+5]
        index += 5
    value = new[index:index+5]
    index += 5
    if not ignore:
        padding = 4 - (index % 4)
        index = index + padding
    return new[index:]


def parse(new, depth, ignore=False):
    #print(new)
    if new == "":
        return ""
    if len(new) < 11:
        return ""
    V = int(new[0:3], 2)
    T = int(new[3:6], 2)
    versions.append(V)
    if T == 4:
        index = 6
        while new[index] == "1":
            value = new[index:index+5]
            index += 5
        value = new[index:index+5]
        index += 5
        if depth == 0:
            padding = 4 - (index % 4)
            index = index + padding
        new = new[index:]
        #print(depth)
    else:
        I = new[6]
        if I == "0":
            L = int(new[7:22], 2)
            if depth == 0:
                new = new[:-2]
            container = new[22:(22+L)]
            while len(container) > 0:
                container = parse(container, depth+1, ignore=True)
            new = new[(22+L):]
        else:
            L = int(new[7:18])
            if depth != 0:
                new = new[18:]
            else:
                new = new[18:-2]
            for _ in range(L):
                new = parse(new, depth+1, ignore=True)

    return new

#new = convert("8A004A801A8002F478")
parse(new, 0)
#value(convert("D2FE28"))
print(sum(versions))
#print(sum(versions))