import helper
with open(helper.nrml("day21.txt")) as f:
    contents = f.read().splitlines()

import functools

pos = list(map(int, [l.split(": ")[1] for l in contents]))
pos = [p-1 for p in pos]
score1 = 0
score2 = 0
mults = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}

def cache(fn):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = fn(*args)
        cache[args] = result
        return result
    return wrapper
    
@cache
def calculate(p1pos, p1score, p2pos, p2score, turn):
    p1 = p2 = 0
    if p1score >= 21:
        p1 = 1
    elif p2score >= 21:
        p2 = 1

    elif turn % 2 == 1:
        for final in range(3, 10):
            if turn == 1: print(final)
            temppos = (p1pos + final) % 10
            tempscore = p1score + temppos + 1
            p1c, p2c = calculate(temppos, tempscore, p2pos, p2score, turn + 1)
            p1 += p1c * mults[final]
            p2 += p2c * mults[final]
    else:
        for final in range(3, 10):
            temppos = (p2pos + final) % 10
            tempscore = p2score + temppos + 1
            p1c, p2c = calculate(p1pos, p1score, temppos, tempscore, turn + 1)
            p1 += p1c * mults[final]
            p2 += p2c * mults[final]
    return p1, p2

p1, p2 = calculate(pos[0], 0, pos[1], 0, 1)
print(p1, p2)