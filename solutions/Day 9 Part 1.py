import helper

with open(helper.nrml("day9.txt")) as f:
    contents = f.read().split("\n")

total = 0
for y in range(len(contents)):
    for x in range(len(contents[0])):
        target = int(contents[y][x])
        if y - 1 >= 0:
            top = int(contents[y - 1][x])
        else:
            top = 99999
        if x > 0:
            left = int(contents[y][x - 1])
        else:
            left = 99999
        if x < (len(contents[0]) - 1):
            right = int(contents[y][x + 1])
        else:
            right = 99999
        if y < len(contents) - 1:
            bottom = int(contents[y + 1][x])
        else:
            bottom = 99999
        if all(target < z for z in [top, right, left, bottom]):
            f = (1 + target)
            #print(y, x, target, [top, right, left, bottom])
            total += f

print(total)