import helper

with open(helper.nrml("day15.txt")) as f:
    contents = f.read().splitlines()

nodes = []

def validate(point):
    y, x = point
    return (0 <= y < len(contents)) and (0 <= x < len(contents[0])) and point in distances


distances = {}
for y in range(len(contents)):
    for x in range(len(contents[0])):
        nodes.append((y, x))
        valid = list(filter(validate, [(y - 1, x), (y, x + 1), (y + 1, x), (y, x - 1)]))
        distances[(y, x)] = {(py, px): int(contents[py][px]) for (py, px) in valid}

unvisited = {node: None for node in nodes} #using None as +inf
visited = {}
current = (0, 0)
currentDistance = 0
unvisited[current] = currentDistance

while True:
    for neighbour, distance in distances[current].items():
        if neighbour not in unvisited: continue
        newDistance = currentDistance + distance
        if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
            unvisited[neighbour] = newDistance
    visited[current] = currentDistance
    del unvisited[current]
    if not unvisited: break
    candidates = [node for node in unvisited.items() if node[1]]
    current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]

print(visited)