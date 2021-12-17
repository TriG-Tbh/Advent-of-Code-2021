import helper

with open(helper.nrml("day17.txt")) as f:
    contents = f.read().splitlines()

contents = contents.split(": ")[1]
x, y = contents.split(", ")
x1, x2 = x.split("=").split("..")
y1, y2 = y.split("=").split("..")

def validate(point):
    return (int(x1) <= point[0] <= int(x2)) and (int(y1) <= point[1] <= int(y2))