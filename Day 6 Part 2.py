import helper

with open(helper.nrml("day6.txt")) as f:
    contents = f.read()

# contents = open("day6.txt").read()

contents = [int(x) for x in contents.split(",")]

vals = {
    8: 0,
    7: 0,
    6: 0,
    5: 0,
    4: 0,
    3: 0,
    2: 0,
    1: 0,
    0: 0
}

for i in contents:
    vals[i] += 1

for _ in range(256):
    zcopy = vals[0]
    for i in range(8):
        vals[i] = vals[i + 1]
    vals[8] = zcopy
    vals[6] += zcopy

print(sum([vals[k] for k in vals.keys()]))