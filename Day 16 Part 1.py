import helper
with open(helper.nrml("day16.txt")) as f:
    contents = f.read()

mapped = {'0': "0000", '1': "0001", '2': "0010", '3': "0011", '4': "0100", '5': "0101", '6': "0110", '7': "0111", '8': "1000", '9': "1001",  'A': "1010", 'B': "1011", 'C': "1100", 'D': "1101", 'E': "1110", 'F': "1111"}

new = ""
for item in contents:
    new += mapped[item]
versions = []


def parse(new, vids, versions):
    print(new)
    lenbits = 0
    lenhex = 0
    startlen = len(new)
    version = int(new[:3], 2)
    versions.append(version)
    new = new[3:]
    
    
    

    typeid = int(new[:3], 2)
    new = new[3:]
    
    if typeid == 4:
        ppart = "1xxxx"
        total = ""
        while ppart[0] == "1":
            ppart = new[:5]
            total = total + ppart
            new = new[5:]
            lenbits += 5
        ppart = new[:5]
        total = total + ppart
        new = new[5:]
        lenbits += 5

        
    else:
        ltid = new[:1]
        new = new[1:]

        lenbits += 1
        length = ""
        #print(ltid)
        print(ltid)
        if ltid == "0":
            length = int(new[:15], 2)
            new = new[15:]
            parse(new[:length], [], versions)
            new = new[length:]
        else:
            length = int(new[:11], 2)
            new = new[11:]
            bp = []
            while len(bp) < length:
                print(" " + new)
                new = parse(new, bp, versions)
                #print(len(bp))
            forward = sum([x[1] for x in bp])
            print(forward)
            versions = versions + [x[0] for x in bp]
            new = new[length:]

    endlen = len(new)
    
    new = new[(4 - (startlen - endlen) % 4):]
    vids.append((version, (startlen - endlen)))
    return new

tempstorage = []

parse(new, tempstorage, versions)
print(versions)
#print(sum(versions))