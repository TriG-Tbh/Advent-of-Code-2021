import helper

with open(helper.nrml("day4.txt")) as f:
    contents = f.read()

import pprint

numbers = [int(x) for x in contents.split("\n")[0].split(",")]
contents = "\n".join(contents.split("\n")[2:])
boards = contents.split("\n\n")

boards = [[[int(x) for x in line.split(" ") if x != ""] for line in b.split("\n")] for b in boards]
zeros = []
for _ in boards:
    zeros.append([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
inside = [[] for b in boards]
outside = [[x for line in b for x in line] for b in boards]

for n in numbers:
    bi = 0
    for b in boards:
        tx = -1
        ty = -1
        for x in range(len(b)):
            for y in range(len(b[0])):
                if b[x][y] == n:
                    tx = x
                    ty = y
                    inside[bi].append(outside[bi][(x * 5 + y)])
                    outside[bi][(tx * 5 + ty)] = 0
                    break
            else:
                continue
            break
        else:
            bi += 1
            continue
        assert (tx != -1) and (ty != -1)
        zeros[bi][tx][ty] = 1
        for x in range(5):
            if all(zeros[bi][x]) or all([zeros[bi][y][x] for y in range(5)]): # all([0, 1]) is treated the same as all([False, True])
                
                break
        else:
            continue
        break
    else:
        continue
    #print(n, bi)

    pulled = [i for line in boards[bi] for i in line]
    pulledzeros = [i for line in zeros[bi] for i in line]
    for x in range(25):
        if pulledzeros[x] == 1:
            pulled[x] = 0

    #pprint.pprint(pulled)
    print(pulled)
    print(pulledzeros)
    print(n * sum(pulled))

    break

