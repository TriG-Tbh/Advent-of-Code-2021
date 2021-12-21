import helper

with open(helper.nrml("day17.txt")) as f:
    contents = f.read()

contents = contents.split(": ")[1]
x, y = contents.split(", ")
x1, x2 = x.split("=")[1].split("..")
y1, y2 = y.split("=")[1].split("..")

x1, x2, y1, y2 = tuple(map(int, [x1, x2, y1, y2]))

maximum = []
def test(x, y):
    probe = [0, 0]
    path = []
    xc = x
    yc = y
    while True:
        probe[0] += x
        probe[1] += y
        if x > 0:
            x -= 1
        elif x < 0:
            x += 1
        y -= 1
        path.append((probe[0], probe[1]))
        if probe[0] > max([x1, x2]) or probe[1] < min([y1, y2]):
            
            break
        if (x1 <= probe[0] <= x2) and (y1 <= probe[1] <= y2):
            maximum.append((xc, yc))
            
            #print(path, x, y)
            #input()
            break


upperbound = 300 # yes. unfortunately, this gives the right answer.
lowerbound = upperbound * -1
for x in range(lowerbound, upperbound+1):
    for y in range(lowerbound, upperbound+1):
        test(x, y)

print(len(maximum))