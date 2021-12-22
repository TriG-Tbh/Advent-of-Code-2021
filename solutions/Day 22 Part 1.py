import helper
with open(helper.nrml("day22.txt")) as f:
    contents = f.read().splitlines()

cubes = set()
i = 0
for line in contents:
    op, vals = line.split(" ")
    vals = [x.split("=")[1] for x in vals.split(",")]
    x1, x2 = map(int, vals[0].split(".."))
    y1, y2 = map(int, vals[1].split(".."))
    z1, z2 = map(int, vals[2].split(".."))

    x1, x2 = min([x1, x2]), max([x1, x2])    
    y1, y2 = min([y1, y2]), max([y1, y2])
    z1, z2 = min([z1, z2]), max([z1, z2])
    if all([f >= -50 for f in [x1, y1, z1]]) and all([f <= 50 for f in [x2, y2, z2]]):
        if op == "on":
            cubes = cubes.union(set([(x, y, z) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1) for z in range(z1, z2 + 1)]))
        else:
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    for z in range(z1, z2 + 1):
                        cubes.discard((x, y, z))
            

    
    i += 1

print(len(cubes))

