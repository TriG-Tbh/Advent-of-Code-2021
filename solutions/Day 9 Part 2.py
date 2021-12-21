import helper

with open(helper.nrml("day9.txt")) as f:
    contents = f.read().split("\n")

lows = []

def validate(point):
    y, x = point
    if y < 0:
        return False
    if x < 0:
        return False
    if x >= len(contents[0]):
        return False
    if y >= len(contents):
        return False
    return int(contents[y][x]) != 9

def branch(point):
    y, x = point
    new = 1
    
    inside = [point]

    newpoints = [point]

    while new != 0:
        copy = []
        for p in newpoints:
            if p not in inside:
                inside.append(p)
            py, px = p
            totest = [(py - 1, px), (py + 1, px), (py, px - 1), (py, px + 1)]
            totest = [np for np in totest if validate(np) and np not in inside] # validate(point) -> point is in board and is not 9
            copy = copy + totest
        
        copy = list(set(copy))
        new = len(copy)
        newpoints = copy.copy()

    return inside


total = 0
for y in range(len(contents)):
    for x in range(len(contents[0])):
        target = int(contents[y][x])
        if y - 1 >= 0:
            top = int(contents[y - 1][x])
        else:
            top = 99999
        if x > 0:
            left = int(contents[y][x - 1])
        else:
            left = 99999
        if x < (len(contents[0]) - 1):
            right = int(contents[y][x + 1])
        else:
            right = 99999
        if y < len(contents) - 1:
            bottom = int(contents[y + 1][x])
        else:
            bottom = 99999
        if all(target < z for z in [top, right, left, bottom]):
            lows.append((y, x))

sizes = {k: len(branch(k)) for k in lows}

vs = list(sizes.values())
m1 = max(vs)
del vs[vs.index(m1)]
m2 = max(vs)
del vs[vs.index(m2)]
m3 = max(vs)
del vs[vs.index(m3)]

print(m1 * m2 * m3)