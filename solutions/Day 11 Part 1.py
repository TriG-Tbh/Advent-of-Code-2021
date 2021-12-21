import helper

with open(helper.nrml("day11.txt")) as f:
    contents = f.read().splitlines()


class Octo:
    def __init__(self, val):
        self.val = val
        self.flashed = False
    

grid = [[Octo(int(c)) for c in line] for line in contents]

global flashes 
flashes = 0

def validate(point):
    y, x = point
    if y < 0:
        return False
    if x < 0:
        return False
    if x >= len(grid[0]):
        return False
    if y >= len(grid):
        return False
    return not(grid[y][x].flashed)

def flash(y, x):
    global flashes
    o = grid[y][x]
    o.flashed = True
    valid = [(y - 1, x - 1), (y + 1, x + 1), (y + 1, x - 1), (y - 1, x + 1), (y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]
    valid2 = list(filter(validate, valid))
 
    for point in valid2:
        ny, nx = point
        
        grid[ny][nx].val += 1
        if grid[ny][nx].val >= 10:
            flash(ny, nx)
    o.val = 0
    flashes += 1

class Octo:
    def __init__(self, val):
        self.val = val
        self.flashed = False

    def __repr__(self):
        return str(self.val)

def fgrid():
    x = []
    for line in grid:
        y = []
        for item in line:
            y.append(item.val)
        x.append(y)
    print(x)

for _ in range(100):
    for ny in range(len(grid)):
        for nx in range(len(grid[0])):
            #print(ny, nx, grid[ny][nx].val)
            grid[ny][nx].val += 1
            #print(ny, nx, grid[ny][nx].val)
            if grid[ny][nx].val >= 10:
                flash(ny, nx)
            #print(grid[ny][nx].flashed)
    for ny in range(len(grid)):
        for nx in range(len(grid[0])):
            if grid[ny][nx].flashed:
                grid[ny][nx].val = 0
                grid[ny][nx].flashed = False

print(flashes)