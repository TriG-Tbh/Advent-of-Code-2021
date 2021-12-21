import helper

with open(helper.nrml("day14.txt")) as f:
    initial, rules = f.read().split("\n\n")
#print(initial)
rules = rules.split("\n")
for _ in range(10):
    
    for r in rules:
        tor, new = r.split(" -> ")
        while tor in initial:
            initial = initial.replace(tor, (tor[0] + new.lower() + tor[1]))
        #print(initial)
    initial = initial.upper()
    #print(len(initial))
#print(initial.count("B"))

letters = {l: initial.count(l) for l in set(initial)}
print(max(letters.values()) - min(letters.values()))
#print([x for x in letters.values()])