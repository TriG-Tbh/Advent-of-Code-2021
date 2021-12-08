import helper

with open(helper.nrml("day8.txt")) as f:
    contents = f.read().split("\n")

# contents = open("day8.txt").read().split("\n")

total = 0

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
    
    pairs[1] = [x for x in lengths[7] if x not in lengths[1]][0] 

    zero = [x for x in first.split(" ") if len(x) == 6]
    four = lengths[4]
    two = lengths[1]
    diff = [x for x in four if x not in two]
    lengths[0] = [x for x in zero if sum([x.count(y) for y in diff]) < 2][0]
    pairs[4] = [x for x in lengths[4] if x not in lengths[0]][0]
    pairs[2] = [x for x in lengths[4] if x != pairs[4] and x not in lengths[1]][0]
    
    threes = [x for x in first.split(" ") if len(x) == 5]
   # print(threes)
    lengths[3] = [x for x in threes if lengths[7][0] in x and lengths[7][1] in x and lengths[7][2] in x][0]
    pairs[7] = [x for x in lengths[3] if x not in lengths[7] and x not in lengths[4]][0]
    
    lengths[5] = [x for x in threes if all([pairs[y] in x for y in [1,2, 4, 7]])][0]

    pairs[6] = [x for x in lengths[5] if x not in [pairs[y] for y in [1, 2, 4, 7]]][0]
    
    pairs[3] = [x for x in lengths[1] if x != pairs[6]][0]

    pairs[5] = [x for x in lengths[8] if x not in pairs.values()][0]

    lengths[0] = "".join([pairs[x] for x in [1, 2, 3, 5, 6, 7]])
    lengths[1] = "".join([pairs[x] for x in [3, 6]])
    lengths[2] = "".join([pairs[x] for x in [1, 3, 4, 5, 7]])
    lengths[3] = "".join([pairs[x] for x in [1, 3, 4, 6, 7]])
    lengths[4] = "".join([pairs[x] for x in [2, 3, 4, 6]])
    lengths[5] = "".join([pairs[x] for x in [1, 2, 4, 6, 7]])
    lengths[6] = "".join([pairs[x] for x in [1, 2, 4, 5, 6, 7]])
    lengths[7] = "".join([pairs[x] for x in [1, 3, 6]])
    lengths[8] = "".join([pairs[x] for x in [1, 2, 3, 4, 5, 6, 7]])
    lengths[9] = "".join([pairs[x] for x in [1, 2, 3, 4, 6, 7]])

    lengths = {"".join(sorted(v)): k for k, v in lengths.items()}
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