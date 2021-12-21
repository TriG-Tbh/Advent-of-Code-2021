import helper

with open(helper.nrml("day15.txt")) as f:
    contents = f.read().splitlines()


def validate(point):
    y, x = point
    return (0 <= y < len(contents)) and (0 <= x < len(contents[0]))


def reconstruct(camefrom, current):
    total = [current]
    while current in camefrom.keys():
        current = camefrom[current]
        total = [current] + total
    return total

def h(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] + p2[1])

def groupadd(line):
    l = [int(x) + 1 for x in line]
    l = [(1 if x > 9 else x) for x in l]
    return "".join(map(str, l))

"""
new = [contents]
for i in range(4):
    new.append([groupadd(line) for line in new[i]])

seg = ["".join([new[i][x] for i in range(len(new))]) for x in range(len(contents))]
for i in range(len(seg * 4)):
    seg.append(groupadd(seg[i]))

contents = seg
"""
nodes = []

for y in range(len(contents)):
    for x in range(len(contents[0])):
        nodes.append((y, x))



def dijkstra(graph, s, t):
    dist = {n: float("inf") for n in nodes}
    prev = {n: None for n in nodes}
    q = set(nodes)
    dist[s] = 0

    while q:
        temp_dist = {k: dist[k] for k in q}
        u = min(temp_dist, key=temp_dist.get)
        q.remove(u)
        if u == t:
            break
        y, x = u
        neighbors = [(ny, nx) for (ny, nx) in [(y - 1, x), (y, x + 1), (y + 1, x), (y, x - 1)] if (0 <= ny < len(contents)) and (0 <= nx < len(contents[0]))]
        for v in neighbors:
            alt = dist[u] + int(contents[u[0]][u[1]])
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u

    s = []
    if (prev[u] is not None) or (u == s):
        while u is not None:
            s.append(u)
            u = prev[u]
    return s


path = dijkstra(contents, (0, 0), (len(contents) - 1, len(contents[0]) - 1))
#print(path)
print(sum([int(contents[py][px]) for (py, px) in path]) - 1)