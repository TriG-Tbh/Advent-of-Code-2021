import helper

with open(helper.nrml("day13.txt")) as f:
    p, i = f.read().split("\n\n")

points = [list(map(int, x.split(","))) for x in p.split("\n")]
#print(points)

instructions = [x.strip("fold along ").split("=") for x in i.split("\n")]

for i in instructions:
    direction, loc = i
    loc = int(loc)
    pos = 0 if direction == "x" else 1
    for point in points:
        if point[pos] < loc:
            diff = loc - point[pos]
            if direction == "x":
                point[pos] += (diff * 2)
            else:
                point[pos] += (diff * 2)
        
        point[pos] -= loc + 1
    
    
points = list(set([tuple(x) for x in points]))
with open(helper.nrml("temp.txt"), "w") as f:
    f.write(str(points)) # use graphing calculator to map points