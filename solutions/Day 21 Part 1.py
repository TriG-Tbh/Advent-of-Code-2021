import helper
with open(helper.nrml("day21.txt")) as f:
    contents = f.read().splitlines()

pos = list(map(int, [l.split(": ")[1] for l in contents]))
pos = [p-1 for p in pos]
score1 = 0
score2 = 0

dice = 0
totalroll = 0

while score1 < 1000 and score2 < 1000:
    for i in range(3):
        dice += 1
        if dice > 100: dice = 1
        pos[0] = (pos[0] + dice) % 10
        
        totalroll += 1
    score1 += pos[0] + 1
    if score1 >= 1000: break
    for i in range(3):
        dice += 1
        if dice > 100: dice = 1
        pos[1] = (pos[1] + dice) % 10
        
        totalroll += 1
    score2 += pos[1] + 1

minimum = min(score1, score2)
#print(minimum)
print(minimum * totalroll)