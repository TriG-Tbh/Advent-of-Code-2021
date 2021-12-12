import helper

with open(helper.nrml("day12.txt")) as f:
    contents = f.read().splitlines()

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
        if (item.lower() != item) or (item.lower() == item and item not in current):
            allowed.append(item)
    for item in allowed:
        path = current + [item]
        if item == "end":
            complete.append(tuple(path))
        else:
            branch(item, path)

branch("start", ["start"])
print(len(complete))