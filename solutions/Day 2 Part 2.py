import helper

with open(helper.nrml("day2.txt")) as f:
    contents = [x.split(" ") for x in f.read().split("\n")]

h = 0
d = 0
a = 0

for z in contents:
    x, y = z
    y = int(y)
    if x == "forward":
        h += y
        d += (a * y)
    if x == "up":
        a -= y
    if x == "down":
        a += y

print(h * d)