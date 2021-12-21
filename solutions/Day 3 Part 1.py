import helper

with open(helper.nrml("day3.txt")) as f:
    contents = f.read().split("\n")

# contents = open("day3.txt").read().split("\n")

gamma = [[x[i] for x in contents] for i in range(len(contents[0]))]
gammastr = "".join(["0" if l.count("0") > l.count("1") else "1" for l in gamma])
gammaint = int(gammastr, 2)

epsilon = [[x[i] for x in contents] for i in range(len(contents[0]))]
epsilonstr = "".join(["0" if l.count("0") < l.count("1") else "1" for l in gamma])
epsilonint = int(epsilonstr, 2)

print(gammaint * epsilonint)