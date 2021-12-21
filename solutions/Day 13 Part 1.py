import helper

with open(helper.nrml("day13.txt")) as f:
    p, i = f.read().split("\n\n")

points = [list(map(int, x.split(","))) for x in p.split("\n")]
#print(points)

instructions = [x.split("=") for x in i.split("\n")]

i = instructions[0]
loc = int(i[1])
for point in points:
    if point[0] < loc:
        diff = loc - point[0]
        point[0] += (diff * 2)
    
points = [tuple(x) for x in points]
print(len(set(points)))