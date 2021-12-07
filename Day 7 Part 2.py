import helper

with open(helper.nrml("day7.txt")) as f:
    contents = [int(x) for x in f.read().split(",")]

# contents = [int(x) for x in open("day7.txt").read().split(",")]

def realval(x):
    return sum(range(1, x + 1))

vals = {x: sum([realval(abs(y - x)) for y in contents]) for x in range(min(contents), max(contents) + 1)}
print(min(vals.values()))