import helper

with open(helper.nrml("day19.txt")) as f:
    contents = f.read().split("\n\n")

def deepcopy(x):
    return [[y for y in line] for line in x]

class Scanner:
    def __init__(self, name, points):
        self.name = name
        self.points = points
        self.facing = 0
        self.rotation = 0
        self.alterx = None
        self.altery = None
        self.alterz = None
        self.pointcopy = deepcopy(points)

    def rotate(self):
        self.points = [[-p[2], p[1], p[0]] for p in self.points]
        self.rotation += 1
        if self.rotation == 4:
            self.rotation = 0
            self.facing += 1
            if self.facing < 4:
                self.points = [[p[1], -p[0], p[2]] for p in self.points]
            elif self.facing == 4:
                self.points = [[p[0], p[2], -p[1]] for p in self.points]
            elif self.facing == 5:
                self.points = [[p[0], -p[2], p[1]] for p in self.points]
                self.points = [[p[0], -p[2], p[1]] for p in self.points]
        
    def intersect(self, other):
        if not isinstance(other, Scanner):
            return [], []
        p1 = deepcopy(self.points)
        p2 = deepcopy(other.points)
        for pp1 in p1:
            for pp2 in p2:
                diffx = pp2[0] - pp1[0]
                diffy = pp2[1] - pp1[1]
                diffz = pp2[2] - pp1[2]
                test = [(p[0] + diffx, p[1] + diffy, p[2] + diffz) for p in p1]
                tocheck = [(x[0], x[1], x[2]) for x in other.points]
                if len(list(set(test) & set(tocheck))) >= 12:
                    self.alterx = diffx
                    self.altery = diffy
                    self.alterz = diffz
                    self.points = test
                    return (test, list(set(test) & set(tocheck)))
        return [], []
    
    def normalized(self):
        return [(x[0] + self.alterx, x[1] + self.altery, x[2] + self.alterz) for x in self.points]

    def __eq__(self, other):
        return self.name == other.name

        
center = None
scanners = []

for item in contents:
    data = item.split("\n")
    name = data[0].strip("---").strip()
    points = [list(map(int, line.split(","))) for line in data[1:]]
    if center is None:
        center = Scanner(name, points)
        center.alterx = 0
        center.altery = 0
        center.alterz = 0
    else:
        scanners.append(Scanner(name, points))

# give this about 3 minutes to run.
# trust me on this one.
# it *can* finish in reasonable time.

total = []
positioned = [center]
while len(scanners) > 0: 
    for s in scanners:
        copy = deepcopy(s.points)
        for pos in positioned:
            s.points = copy
            s.facing = 0
            s.rotation = 0
            intersection = []
            for _ in range(25):
                s.rotate()
                intersection, intersected = s.intersect(pos)
                if len(intersection) > 0:
                    break
            if len(intersection) > 0:
                positioned.append(s)
                scanners.remove(s)
                break

total = []
for item in positioned:
    total.append((item.alterx, item.altery, item.alterz))

points = list(set(total))
maximum = 0
for p1 in points:
    for p2 in points:
        if (abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])) > maximum:
            maximum = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])
print(maximum)