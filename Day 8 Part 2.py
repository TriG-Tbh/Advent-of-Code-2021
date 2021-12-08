import helper

with open(helper.nrml("day8.txt")) as f:
    contents = [int(x) for x in f.read().split("\n")]
