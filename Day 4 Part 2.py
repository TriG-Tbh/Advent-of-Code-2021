import helper

with open(helper.nrml("day4.txt")) as f:
    contents = f.read()

import pprint
import numpy

# contents = open("day3.txt").read().split("\n")

numbers = [int(x) for x in contents.split("\n")[0].split(",")]
contents = "\n".join(contents.split("\n")[2:])
boards = contents.split("\n\n")

boards = [[int(x) for line in b.split("\n") for x in line.split(" ") if x != ""] for b in boards]
copy = boards.copy()
winners = []

def chunks(l, n):
    for i in range(0, n):
        yield l[i::n]

zeros = []
for b in boards:
    zeros.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

for b in boards:
    c = b.copy()
    for n in numbers:
        if n in c:
            c[c.index(n)] = 0
            chunkedz = [c[i:i+5] for i in range(0, len(c), 5)]
        for x in range(5):
            if not (any(chunkedz[x]) or any([chunkedz[y][x] for y in range(5)])):
                winners.append(c)

boards = boards[::-1]
numbers = numbers[::-1]
winners = winners[::-1]

for n in numbers:
    bi = 0
    for b in boards:
        w = winners[bi]
        if n in b:
            index = b.index(n)
            w[index] = n
            
            zeros[bi][index] = 0
            chunkedz = [zeros[bi][i:i+5] for i in range(0, len(zeros[bi]), 5)]
            #pprint.pprint(chunkedz)
            rows = []
            cols = []
            for x in range(5):
                rows.append(all(chunkedz[x]))
                cols.append(all([chunkedz[y][x] for y in range(5)]))
            rows = [not(v) for v in rows]
            cols = [not(v) for v in cols]
            if all(rows) and all(cols):
                pulled = [boards[bi][i] for i in range(25) if zeros[bi][i] == 0]
                pulled.remove(n)
                print(sum(pulled) * n)
                break
        bi += 1
    else:
        continue
    break