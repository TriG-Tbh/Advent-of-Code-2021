import helper

with open(helper.nrml("day2.txt")) as f:
    contents = [x.split(" ") for x in f.read().split("\n")]

h = 0
w = 0
for z in contents:
    x, y = z
    y = int(y)
    if x == "forward":
        w += y
    if x == "up":
        h -= y
    if x == "down":
        h += y

print(h * w)