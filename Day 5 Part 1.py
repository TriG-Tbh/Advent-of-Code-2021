import helper
with open(helper.nrml("day5.txt")) as f:
    contents = f.read().split("\n")

contents = [x.split(" -> ") for x in contents]
contents = [[tuple(map(int, y.split(","))) for y in z] for z in contents]


ranges = []
intersections = []

points = []


for line in contents:
    x1, y1 = line[0]
    x2, y2 = line[1]

    
    
    if x2 == x1 or y2 == y1:
        ranges.append(line)

for line in ranges:
    p = []
    maxx = max(line[0][0], line[1][0])
    minx = min(line[0][0], line[1][0])
    maxy = max(line[0][1], line[1][1])
    miny = min(line[0][1], line[1][1])
    for x in range(maxx - minx + 1):
        for y in range(maxy - miny + 1):
            p.append((minx + x, miny + y))
    points.append(p)

for base in points:
    for target in points:
        if base != target:
            inter = list(set(base).intersection(set(target))) # this is like the only thing that doesnt take entire minutes to complete
            intersections = intersections + inter

print(len(set(intersections))) 
            
