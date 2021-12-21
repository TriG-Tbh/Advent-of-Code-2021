import helper

with open(helper.nrml("day8.txt")) as f:
    contents = f.read().split("\n")

contains = 0
for line in contents:
    separate = line.split(" | ")[1]
    lists = list(map(len, separate.split(" ")))
    for item in [2, 3, 4, 7]:
        if item in lists:
            contains += lists.count(item)

    

print(contains)