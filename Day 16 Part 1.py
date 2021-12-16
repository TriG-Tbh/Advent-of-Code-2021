import helper
with open(helper.nrml("day16.txt")) as f:
    contents = f.read()

mapped = {'0': "0000", '1': "0001", '2': "0010", '3': "0011", '4': "0100", '5': "0101", '6': "0110", '7': "0111", '8': "1000", '9': "1001",  'A': "1010", 'B': "1011", 'C': "1100", 'D': "1101", 'E': "1110", 'F': "1111"}

new = ""
for item in contents:
    new += mapped[item]

versions = []
while new != "":

    lenbits = 0
    lenhex = 0

    version = int(new[:3], 2)
    new = new[3:]
    versions.append(version)
    
    lenbits += 3

    typeid = int(new[:3], 2)
    new = new[3:]
    lenbits += 3
    
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

        new = new[(4 - lenbits % 4):]
    else:
        ltid = new[:1]
        new = new[1:]

        lenbits += 1
        length = ""
        if ltid == "1":
            length = new[:15]
            new = new[15:]
            lenbits += 15
        else:
            length = new[:11]
            new = new[11:]
            lenbits += 11
        