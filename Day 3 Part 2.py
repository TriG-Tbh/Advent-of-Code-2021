import helper

with open(helper.nrml("day3.txt")) as f:
    contents = f.read().split("\n")
    contents = sorted(contents)

# contents = open("day3.txt").read().split("\n")

ogr = 0
elim = contents.copy()
for i in range(len(contents[0])):
    proc = [x[i] for x in elim]
    maxval = "0" if proc.count("0") > proc.count("1") else "1"
    elim = [e for e in elim if e[i] == maxval]
    if len(elim) == 1:
        ogr = int(elim[0], 2)
        break

csr = 0
elim = contents.copy()
for i in range(len(contents[0])):
    proc = [x[i] for x in elim]
    maxval = "1" if proc.count("1") < proc.count("0") else "0"
    elim = [e for e in elim if e[i] == maxval]
    if len(elim) == 1:
        csr = int(elim[0], 2)
        break

print(ogr * csr)