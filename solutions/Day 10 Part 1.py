import helper

with open(helper.nrml("day10.txt")) as f:
    contents = f.read().split("\n")

mapped = {
    "(": ")",
    "<": ">",
    "{": "}",
    "[": "]"
}

worth = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

inc = []

summed = 0
for item in contents:
    x = []
    go = True
    for c in item:
        if c in mapped.keys():
            x.append(c)
        if c in mapped.values():
            if c == mapped[x[-1]]:
                del x[-1]
            else:
                summed += worth[c]
                go = False
                break
print(summed)
