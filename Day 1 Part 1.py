import helper

with open(helper.nrml("day1.txt")) as f:
    contents = [int(x) for x in f.read().split("\n")]

total = 0

for x in range(1, len(contents) - 1):
    if contents[x] > contents[x - 1]:
        total += 1

print(total)