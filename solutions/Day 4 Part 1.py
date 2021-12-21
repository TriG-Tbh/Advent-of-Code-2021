import helper

with open(helper.nrml("day4.txt")) as f:
    contents = f.read()


# contents = open("day3.txt").read().split("\n")

numbers = [int(x) for x in contents.split("\n")[0].split(",")]
contents = "\n".join(contents.split("\n")[2:])
boards = contents.split("\n\n")

boards = [[int(x) for line in b.split("\n") for x in line.split(" ") if x != ""] for b in boards]
copy = boards.copy()
zeros = []
for _ in boards:
    zeros.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

def chunks(l, n):
    for i in range(0, n):
        yield l[i::n]

for n in numbers:
    bi = 0
    for b in boards:
        if n in b:
            index = b.index(n)
            b[index] = 0
            zeros[bi][index] = 1
            chunkedz = [zeros[bi][i:i+5] for i in range(0, len(zeros[bi]), 5)]
        for x in range(5):
            if all(chunkedz[x]) or all([chunkedz[y][x] for y in range(5)]): # today I learned all([0, 1]) is treated as all([False, True])
                print(sum(b) * n)
                break
        else:
            bi += 1
            continue
        break
               
    else:
        continue
    break