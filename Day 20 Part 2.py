import helper
with open(helper.nrml("day20.txt")) as f:
    alg, image = f.read().strip().split("\n\n")

# this one takes a while.
# and by that, i mean 15-20 minutes.
# probably (a lot) more, maybe a little less.
# so sit back, relax, grab a good book, and give this one a *lot* more time than normal.

points = []
newpoints = []

image = image.split("\n")

for y in range(len(image)):
    for x in range(len(image[0])):
        if image[y][x] == "#":
            points.append((y, x))

pad = 2

for z in range(25):
    newpoints = []
    miny = min([x[0] for x in points]) - pad
    minx = min([x[1] for x in points]) - pad
    maxy = max([x[0] for x in points]) + pad
    maxx = max([x[1] for x in points]) + pad

    for y in range(miny - 1, maxy + 2):
        for x in range(minx - 1, maxx + 2):
            valid = [(y + newy, x + newx) for newy in range(-1, 2) for newx in range(-1, 2)]
            stringrep = ""
            for point in valid:
                if point not in points:
                    stringrep = stringrep + "0"
                else:
                    stringrep = stringrep + "1"
            intrep = int(stringrep, 2)
            if alg[intrep] == "#":
                newpoints.append((y, x))
    points = [x for x in newpoints]

    newpoints = []
    miny = min([x[0] for x in points]) - pad
    minx = min([x[1] for x in points]) - pad
    maxy = max([x[0] for x in points]) + pad
    maxx = max([x[1] for x in points]) + pad

    for y in range(miny - 1, maxy + 2):
        for x in range(minx - 1, maxx + 2):
            valid = [(y + newy, x + newx) for newy in range(-1, 2) for newx in range(-1, 2)]
            stringrep = ""
            for point in valid:
                if point in points:
                    stringrep = stringrep + "1"
                else:
                    if (y < miny or y > maxy) or (x < minx or x > maxx):
                        stringrep = stringrep + "1"
                    else:
                        stringrep = stringrep + "0"
            intrep = int(stringrep, 2)
            if alg[intrep] == "#":
                newpoints.append((y, x))
    points = [x for x in newpoints]   

    points = [x for x in points if (-2 * (z + 1)) <= x[0] < len(image) + (2 * (z + 1)) and (-2 * (z + 1)) <= x[1] < len(image[0]) + (2 * (z + 1))] 

print(len(points))
