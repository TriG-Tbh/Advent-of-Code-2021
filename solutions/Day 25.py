import helper
with open(helper.nrml("day25.txt")) as f:
    contents = [[x for x in line] for line in f.read().splitlines()]


# merry christmas
# feliz navidad
# it's been a real fun ride through all 25 days
# huge shoutout to the people over at pydis (https://discord.gg/python btw)
# each of you are amazing
# thanks to eric for making the calendar itself
# it's amazing that you can put hundreds of thousands of coders through puzzle hell, while making it a fun (and sometimes collaborative) group experience
# this year has been super fun, and i can't wait for next year

def deepcopy(l):
    return [[x for x in line] for line in l]

step = 1
while True:
    done = 0
    moved = []
    valid = []
    #copy = deepcopy(contents)
    for y in range(len(contents)):
        for x in range(len(contents[0])):
            if (y, x) in moved:
                continue
            wraparound = (x + 1) % len(contents[0])
            if contents[y][x] == ">" and contents[y][wraparound] == ".":
                valid.append((y, x))
                done += 1

    for move in valid:
        y, x = move
        contents[y][(x + 1) % len(contents[0])] = ">"
        contents[y][x] = "."

    
    valid = []
    for y in range(len(contents)):
        
        for x in range(len(contents[0])):
        
            if (y, x) in moved:
                continue
            wraparound = (y + 1) % len(contents)
            if contents[y][x] == "v" and contents[wraparound][x] == ".":
                valid.append((y, x))
                done += 1
    for move in valid:
        y, x = move
        contents[(y + 1) % len(contents)][x] = "v"
        contents[y][x] = "."
    
    if done == 0:
         print(step); break
         

    step += 1


