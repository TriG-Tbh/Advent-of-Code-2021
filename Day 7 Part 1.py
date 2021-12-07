import helper

with open(helper.nrml("day7.txt")) as f:
    contents = [int(x) for x in f.read().split(",")]

vals = {x: sum([abs(x - y) for y in contents]) for x in contents}
print(min(vals.values()))