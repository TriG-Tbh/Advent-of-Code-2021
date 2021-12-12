import helper

with open(helper.nrml("day12.txt")) as f:
    contents = f.read().splitlines()

# contents = open("day12.txt").read().splitlines()

linked = {}

for line in contents:
    start, end = line.split("-")
    if start not in linked.keys():
        linked[start] = []
    linked[start].append(end)
    if end not in linked.keys():
        linked[end] = []
    linked[end].append(start)

global complete
complete = []

def branch(location, current):
    complete
    copy = current.copy()
    allowed = []
    for item in linked[location]:
        if item != "start":
            if item.lower() != item:
                allowed.append(item)
            else:
                try:
                    lower = [x for x in current if x.lower() == x]
                except:
                    print(current)
                    raise
                counted = {current.count(x): x for x in lower}
                if 2 in counted.keys():
                    if item not in current:
                        allowed.append(item)
                else:
                    allowed.append(item)
    for item in allowed:
        path = current + [item]
        if item == "end":
            complete.append(tuple(path))
        else:
            branch(item, path)

branch("start", ["start"])
print(len(complete))