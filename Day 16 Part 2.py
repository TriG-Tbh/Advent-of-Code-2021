import helper
with open(helper.nrml("day16.txt")) as f:
    contents = f.read()


# contents = 'CE00C43D881120'

# if anyone decides to look at this,
# i'm sorry in advance.
# i truly am.

mapped = {'0': "0000", '1': "0001", '2': "0010", '3': "0011", '4': "0100", '5': "0101", '6': "0110", '7': "0111",
          '8': "1000", '9': "1001", 'A': "1010", 'B': "1011", 'C': "1100", 'D': "1101", 'E': "1110", 'F': "1111"}


def convert(fromstr):
    new = ""
    for item in fromstr:
        new += mapped[item]
    return new


new = convert(contents)


def addi(params):
    return sum(params)


def prod(params):
    total = 1
    for x in params:
        total *= x
    return total


def mini(params):
    return min(params)


def maxi(params):
    return max(params)


def grea(params):
    return int(params[0] > params[1])


def less(params):
    return int(params[0] < params[1])


def equa(params):
    return int(params[0] == params[1])


execution = []


def parse(new, depth, execution, ignore=False):
    if new == "":
        return ""
    if len(new) < 11:
        return ""
    V = int(new[0:3], 2)
    T = int(new[3:6], 2)
    if T == 4:
        index = 6
        total_val = ''
        while new[index] == "1":
            value = new[index + 1:index + 5]
            total_val += value
            index += 5
        value = new[index + 1:index + 5]
        index += 5
        total_val += value
        execution.append(str(int(total_val, 2)))
        
        new = new[index:]

        execution.append(",")

    else:
        I = new[6]

        ftype = {0: "addi", 1: "prod", 2: "mini", 3: "maxi", 5: "grea", 6: "less", 7: "equa"}[T]

        execution.append("" + ftype + "([")

        if I == "0":
            L = int(new[7:22], 2)
            
            container = new[22:(22 + L)]
            while len(container) > 0:
                container = parse(container, depth + 1, execution, ignore=True)
            new = new[(22 + L):]
            execution.append("]),")
        else:
            L = int(new[7:18], 2)
            new = new[18:]
            for _ in range(L):
                new = parse(new, depth + 1, execution, ignore=True)
            execution.append("]),")
    return new


# new = convert("A0016C880162017C3686B18A3D4780")
parse(new, 0, execution)
created = "(" + "".join(execution).rstrip(",").replace(",]", "]").replace(",", ", ") + ")"
print(eval(created))