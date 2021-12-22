import helper
with open(helper.nrml("day22.txt")) as f:
    contents = f.read().splitlines()

cubes = {}
i = 0
total = 0

for line in contents:
    toadd = {}
    op, vals = line.split(" ")
    vals = [x.split("=")[1] for x in vals.split(",")]
    x1, x2 = map(int, vals[0].split(".."))
    y1, y2 = map(int, vals[1].split(".."))
    z1, z2 = map(int, vals[2].split(".."))

    x1, x2 = min([x1, x2]), max([x1, x2])    
    y1, y2 = min([y1, y2]), max([y1, y2])
    z1, z2 = min([z1, z2]), max([z1, z2])
    

    for (sx1, sx2, sy1, sy2, sz1, sz2), c in cubes.items():
        ix1 = max(sx1, x1)
        ix2 = min(sx2, x2)
        iy1 = max(sy1, y1)
        iy2 = min(sy2, y2)
        iz1 = max(sz1, z1)
        iz2 = min(sz2, z2)
       

        if ix1 <= ix2 and iy1 <= iy2 and iz1 <= iz2:
            if (ix1, ix2, iy1, iy2, iz1, iz2) not in toadd:
                toadd[(ix1, ix2, iy1, iy2, iz1, iz2)] = 0
            
            toadd[(ix1, ix2, iy1, iy2, iz1, iz2)] -= c # forgot that sometimes they can have *more* than one

    if op == "on":
        if (x1, x2, y1, y2, z1, z2) not in toadd:
            toadd[(x1, x2, y1, y2, z1, z2)] = 0
        toadd[(x1, x2, y1, y2, z1, z2)] += 1
    for (cx1, cx2, cy1, cy2, cz1, cz2), count in toadd.items():
        if (cx1, cx2, cy1, cy2, cz1, cz2) not in cubes:
            cubes[(cx1, cx2, cy1, cy2, cz1, cz2)] = 0
        cubes[(cx1, cx2, cy1, cy2, cz1, cz2)] += count

    i += 1

total = 0
for (x1, x2, y1, y2, z1, z2), count in cubes.items():
    total += (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1) * count

print(total)