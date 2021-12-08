import helper

with open(helper.nrml("day8.txt")) as f:
    contents = f.read().split("\n")

total = 0

def diffstr(s1, s2):
    if len(s1) > len(s2):
        return len([i for i in s1 if i not in s2])
    else:
        return len([i for i in s2 if i not in s1])

index = 0
for line in contents:
    lengths = {0: "", 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: ""}
    pairs = {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: ""}

    first, last = line.split(" | ")
    combo = first.split(" ") + last.split(" ")

    for x in [(1, 2), (7, 3), (4, 4), (8, 7)]:
        item = x[1]
        if item in list(map(len, combo)):
            iindex = list(map(len, combo)).index(item)
            lengths[x[0]] = "".join(sorted(combo[iindex]))
    
    # 1 -> "a", 2 -> "b", etc. as given in first display in problem
    pairs[1] = [x for x in lengths[7] if x not in lengths[1]][0] # any character used in 1, not used in 7, must be top one

    zero = [x for x in first.split(" ") if len(x) == 6]
    four = lengths[4]
    two = lengths[1]
    diff = [x for x in four if x not in two]
    lengths[0] = [x for x in zero if sum([x.count(y) for y in diff]) < 2][0]
    pairs[4] = [x for x in lengths[4] if x not in lengths[0]][0]

    pairs[2] = [x for x in lengths[4] if x != pairs[4] and x not in lengths[1]][0]

    six = [x for x in first.split(" ") if len(x) == 6]
    
    lengths[6] = [x for x in six if not(lengths[1][0] in x and lengths[1][1] in x)][0]
    lengths[9] = [x for x in six if x != lengths[6] and pairs[4] in x][0]
    lengths[5] = [x for x in first.split(" ") if len(x) == 5 and pairs[2] in x][0]

    pairs[6] = [x for x in lengths[5] if x in lengths[1]][0]
    lengths[2] = [x for x in first.split(" ") if len(x) == 5 and pairs[6] not in x][0]
    lengths = {k: "".join(sorted(v)) for k, v in lengths.items()}
    lengths[3] = ["".join(sorted(x)) for x in first.split(" ") if "".join(sorted(x)) not in lengths][0]
    lengths = {v: k for k, v in lengths.items()}
    t = 0
    for item in last.split(" "):
        item = "".join(sorted(item))
        try:
            t = t * 10 + lengths[item]
        except:
            print(lengths)
            raise
    total += t
    index += 1

print(total)