import helper

with open(helper.nrml("day15.txt")) as f:
    contents = f.read().splitlines()

included = {}

def validate(point, path):
    y, x = point
    return (0 <= y < len(contents)) and (0 <= x < len(contents[0])) and (point not in path)



distances = {}
for y in range(len(contents)):
    for x in range(len(contents[0])):
        if y == x == 0:
            distances[(y, x)] = 0
        else:
            distances[(y, x)] = 999999999999999999

cd = 0
current = ()

def validate(point):
    y, x = point
    return (0 <= y < len(contents)) and (0 <= x < len(contents[0])) and point in unvisited

while (len(contents) - 1, len(contents[0]) - 1) in unvisited:

    y, x = current
    valid = list(filter(validate, [(y - 1, x), (y, x + 1), (y + 1, x), (y, x - 1)]))
    point_distance = {}
    for p in valid:
        py, px = p
        newd = distances[current] + int(contents[py][px])
        if newd < distances[p]:
            distances[p] = newd
        point_distance[p] = distances[p]
    
    points = list(point_distance.keys())
    points.sort(key=lambda x: point_distance[x])
    del unvisited[current]
    #print(points)
    if not unvisited:
        break
    current = points[0]


        

print(included)