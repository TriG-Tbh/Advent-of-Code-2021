import helper

with open(helper.nrml("day1.txt")) as f:
    contents = [int(x) for x in f.read().split("\n")]

total = 0

for x in range(1, len(contents) - 0):
    if sum(contents[(x-1):(x+2)]) < sum(contents[x:(x+3)]):
        total += 1

print(total)