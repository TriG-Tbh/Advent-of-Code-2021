import helper, pprint

with open(helper.nrml("bonus.txt")) as f:
    contents = f.read().splitlines()

n = int(contents[0])
arr = [[y for y in x] for x in contents[1:]]
print(arr)

length = len(arr[0])
height = len(arr)

def validate(point):
    y, x = point
    if y < 0:
        return False
    if x < 0:
        return False
    if x >= len(arr[0]):
        return False
    if y >= len(arr):
        return False
    return True

def explode(point):
    y, x = point
    valid = [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]
    valid2 = list(filter(validate, valid))
    arr[y][x] = "X"
    for p in valid2:
        py, px = p
        if arr[py][px] == "9":
            explode(p)
        arr[py][px] = "X"

i = 0
import os
while True:
    p = 0
    os.system("cls")
    while p < n:
        px = i % length
        py = i // length
        i += 1
        try:
            if arr[py][px] != "X":
                p += 1
        except IndexError:
            i -= (length * height) + 1
            continue
    
    if arr[py][px] == "9":
        explode((py, px))
    arr[py][px] = "X"
    pprint.pprint(arr)
    print(py, px)
    input()