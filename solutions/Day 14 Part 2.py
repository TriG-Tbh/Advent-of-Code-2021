import helper

with open(helper.nrml("day14.txt")) as f:
    initial, rules = f.read().split("\n\n")
#print(initial)

singles = {}
pairs = {}

rules = rules.split("\n")
for r in rules:
    try:
       tor, new = r.split(" -> ")
    except:
        print(r)
        raise
    singles[tor[0]] = initial.count(tor[0])
    singles[tor[1]] = initial.count(tor[1])
    singles[new] = initial.count(new)
    pairs[tor[0] + new] = initial.count(tor[0] + new)
    pairs[new + tor[1]] = initial.count(new + tor[1])
    pairs[tor] = initial.count(tor)

def addto(d, key, value):
    if key not in d.keys():
        d[key] = 0
    d[key] += value
    return d

for _ in range(40):
    for r in rules:
        tor, new = r.split(" -> ")
        x, y = (z for z in tor)
        
        pairs = addto(pairs, x + new.lower(), pairs[tor])
        
        pairs = addto(pairs, new.lower() + y, pairs[tor])
        
        
        singles[new.upper()] += pairs[tor]
        
        
        pairs[tor] = 0
        
        
    #print({k: v for k, v in pairs.items() if v > 0})
    
    for item in pairs.keys():
        test = item.upper()
        if test != item:
            pairs[test] += pairs[item]
            pairs[item] = 0
    #print({k: v for k, v in pairs.items() if v > 0})
    #input()
    #print(pairs)
    
letters = singles
#print(letters)

print(max(letters.values()) - min(letters.values()))
#print([x for x in letters.values()])