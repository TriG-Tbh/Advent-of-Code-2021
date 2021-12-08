import helper

with open(helper.nrml("day7.txt")) as f:
    contents = [int(x) for x in f.read().split(",")]

# contents = [int(x) for x in open("day7.txt").read().split(",")]

def realval(x):
    return (x ** 2 + x) / 2

vals = {x: sum([realval(abs(y - x)) for y in contents]) for x in range(min(contents), max(contents) + 1)}
print(int(min(vals.values())))