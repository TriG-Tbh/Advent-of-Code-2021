import helper
with open(helper.nrml("day24.txt")) as f:
    contents = f.read().splitlines()

variables = {
    "x": 0,
    "y": 0,
    "z": 0
}

l5s = []
l6s = []
l16s = []
# load
for i in range(14):
    try:
        l5s.append(int(contents[18 * i - 1 + 5].split(" ")[2]) == 1)
    except:
        print(i * 5 - 1)
        raise
    l6s.append(int(contents[18 * i - 1 + 6].split(" ")[2]))
    l16s.append(int(contents[18 * i - 1 + 16].split(" ")[2]))

loads = []
for x in range(14):
    loads.append((l5s[x], l6s[x], l16s[x]))

def solve(values, z=0):
    if len(values) == 0 and z == 0:
        return ""
    try:
        line5, line6, line16 = values[0]
    except:
        print(values)
        print(z)
        raise
    if line5:
        for w in list(range(1, 10))[::-1]:
            result = solve(values[1:], z * 26 + line16 + w)
            if result is not None:
                return str(w) + result
    else:
        newdigit = (z % 26) + line6
        if not 1 <= newdigit <= 9:
            return None
        result = solve(values[1:], z // 26)
        if result is not None:
            return str(newdigit) + result
    return None

print(solve(loads))