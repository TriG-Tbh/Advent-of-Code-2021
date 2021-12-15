import helper

with open(helper.nrml("day15.txt")) as f:
    contents = f.read().splitlines()

included = {}

def validate(point, path):
    y, x = point
    return (0 <= y < len(contents)) and (0 <= x < len(contents[0])) and (point not in path)

def branch(point, path, depth=0):
    #if depth == 0:
    #print(depth)
    y, x = point
    if point not in path:
        path.append(point)
    valid2 = [p for p in [(y - 1, x), (y, x + 1), (y + 1, x), (y, x - 1)] if validate(p, path.copy())]
    #print(valid2)   
    valid2.sort(key=lambda i: int(contents[i[0]][i[1]]))
    #print(valid2)
    #input()
    for p in valid2:
        
        py, px = p
        if py == len(contents) - 1 and px == len(contents[0]) - 1:
            pathnum = [contents[zy][zx] for zy, zx in path]
            included["".join(pathnum)] = sum([int(f) for f in pathnum])
            #print(pathnum)
            break
        else:
            branch(p, path.copy(), depth=depth+1)

branch((0, 0), [(0, 0)])

print(included)