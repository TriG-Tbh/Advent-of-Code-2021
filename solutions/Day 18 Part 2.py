import helper

with open(helper.nrml("day18.txt")) as f:
    contents = f.read().splitlines()

def magnitude(string_rep):
    list_form = eval(string_rep)
    index = 0
    for index in range(2):
        value = list_form[index]
        if isinstance(value, list):
            value = magnitude(str(value))
            list_form[index] = value
    return (list_form[0] * 3) + (list_form[1] * 2)

def floor(value):
    return int(value // 1)

def ceil(value):
    if float(value) % 1 == 0:
        return int(value)
    else:
        return int(value) + 1

def explode(string_rep):
    string_rep = string_rep.replace(" ", "")
    index = 0
    nested = 0
    reduced = False
    while index < len(string_rep):
        if string_rep[index] == "[":
            nested += 1
        if string_rep[index] == "]":
            nested -= 1
            if nested >= 4: # hoping that there will never be something nested more than 5 times
                reduced = True
                last = string_rep[:index]
                rindex = last.rfind("[")
                nums = last[(rindex+1):]
                try:
                    n1, n2 = tuple(map(int, nums.split(",")))
                except:
                    print(string_rep)
                    raise

                part1 = ""
                intfind = [x for x in string_rep[:rindex]]
                for i in range(len(intfind)):
                    i = rindex - i - 1
                    if intfind[i].isnumeric():
                        v = intfind[i]
                        todel = False
                        if intfind[i-1].isnumeric():
                            v = intfind[i-1] + v
                            todel = True
                        intfind[i] = str(int(v) + n1)
                        if todel:
                            del intfind[i-1]
                        break
                part1 = "".join(intfind)

                part2 = ""
                intfind2 = [x for x in string_rep[(index+1):]]
                for i in range(len(intfind2)):
                    if intfind2[i].isnumeric():
                        v = intfind2[i]
                        todel = False
                        if intfind2[i+1].isnumeric():
                            v = v + intfind2[i+1]
                            todel = True
                        intfind2[i] = str(int(v) + n2)
                        if todel:
                            del intfind2[i+1]
                        break
                part2 = "".join(intfind2)
                string_rep = part1 + "0" + part2
                
                index -= 4
                return (string_rep.replace(" ", ""), reduced)

        index += 1 
    return (string_rep.replace(" ", ""), reduced)

def split(string_rep):
    string_rep = string_rep.replace(" ", "")
    index = 0
    reduced = False
    while index < len(string_rep) - 1:
        if string_rep[index].isnumeric() and string_rep[index + 1].isnumeric():
            val = int(string_rep[index] + string_rep[index + 1])
            insert = "[" + str(floor(val / 2)) + "," + str(ceil(val / 2)) + "]"
            string_rep = string_rep[:index] + insert + string_rep[(index+2):]
            index += 4
            reduced = True
            return (string_rep.replace(" ", ""), reduced)
        index += 1
        
    return (string_rep.replace(" ", ""), reduced)
    

def handle(string_rep):
    string_rep, reduced = explode(string_rep)
    if not reduced:
        string_rep, reduced = split(string_rep)
    
    return (string_rep.replace(" ", ""), reduced)

def snailfish_add(l1, l2):
    list1 = eval(l1) # don't try this at home, kids
    list2 = eval(l2)

    new = [list1] + [list2]
    reduced = True
    while reduced:
        new, reduced = handle(str(new))
    return str(new).replace(" ", "")

possible = []
for i1 in range(len(contents)):
    for i2 in range(len(contents)):
        if i1 != i2:
            possible.append((contents[i1], contents[i2]))
possible = list(set(possible))
m = 0
for i in range(len(possible)):
    item = possible[i]
    test = magnitude(snailfish_add(item[0], item[1])) # give this a minute to run. trust me, it runs in reasonable time.
    if test > m:
        m = test
print(m)