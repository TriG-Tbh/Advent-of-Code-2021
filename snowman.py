# Run as:
# snowman(n, arr)
def snowman(n: int, arr: list) -> tuple:
    """
    A function that passes the Christmas challenge

    Parameters
    ---
    n        (int): Step for elimination
    arr     (list): Grid of elements to comb through
                    Should be a multidimensional array such as
                        Each line of the grid split into its individual characters (as integers)
                        [[int, int, int], [int, int, int], ...]
                    or
                        Each line of the grid split into its individual characters (as strings)
                        [[str, str, str], [str, str, str], ...]
                    or
                        Each line of the grid in its own list
                        [[str], [str], [str], ...]
    Returns
    ---
    return (tuple): Tuple containing the points of the snowman and Santa
                    (will give None as a point if the entity not found)
    Example Usage
    ---
    snowman(3, [["0006060066"], ["6900696600"], ["0000990006"], ["6060906606"]]) -> ((0, 6), (2, 9))
    """
    if isinstance(arr[0][0], int):
        arr = [[str(x) for x in line] for line in arr]

    if len(arr[0]) == 1:
        arr = [[x for x in str(line[0])] for line in arr]

    arr = [[str(x) for x in line] for line in arr] # sanity check
    length = len(arr[0])
    height = len(arr)
    def validate(point):
        y, x = point
        if y < 0:
            return False
        if x < 0:
            return False
        if x >= len(arr[0]):
            return False
        if y >= len(arr):
            return False
        return True

    def explode(point):
        y, x = point
        valid = [(y - 1, x), (y, x + 1), (y + 1, x), (y, x - 1)]
        valid2 = list(filter(validate, valid))
        arr[y][x] = "X"
        for p in valid2:
            py, px = p
            flattened = [x for line in arr for x in line]
            if arr[py][px] == "9":
                explode(p)
            else:
                if flattened.count(arr[py][px]) > 1:
                    arr[py][px] = "X"
                    flattened = [x for line in arr for x in line]

    i = 0
    flattened = [x for line in arr for x in line]


    while True:
        p = 0
        while p < n:
            px = i % length
            py = i // length
            i += 1
            if i >= (length * height):
                i -= (length * height) + 1
                continue
            if arr[py][px] != "X":
                p += 1


        if arr[py][px] == "9":
            explode((py, px))
        val = arr[py][px]

        if val == "6" or val == "0":
            flattened = [x for line in arr for x in line]
            if flattened.count(val) > 1:
                arr[py][px] = "X"
        copy = [x for line in arr for x in line]
        if copy == flattened:
            break

    flattened = [x for line in arr for x in line]
    for item in ["0", "6"]:
        while flattened.count(item) > 1:
            i = flattened[::-1].index(item)
            i = (len(flattened) - 1 - i)
            px = i % length
            py = i // length
            arr[py][px] = "X"
            flattened = [x for line in arr for x in line]

    """for y in range(len(arr)):
        y = height - y - 1
        for x in range(len(arr[0])):
            x = length - x - 1
            val = arr[y][x]
            if val == "6" or val == "0":
                if flattened.count(val) > 1:
                    arr[y][x] = "X"
                    flattened = [x for line in arr for x in line]"""

    inside = []
    flattened = [x for line in arr for x in line]

    for item in ["0", "6"]:
        if item not in flattened:
            inside.append(None)
            continue
        i = flattened.index(item)
        px = i % length
        py = i // length
        inside.append((py, px))

    """for y in range(len(arr)):
        for x in range(len(arr[0])):
            if arr[y][x] == "6" or arr[y][x] == "0":
                inside.append((y, x))"""



    inside = tuple(inside)
    return inside

print(snowman(3, [
[0,0,0,6,0,6,0,0,6,6],
[6,9,0,0,6,9,6,6,0,0],
[0,0,0,0,9,9,0,0,0,6],
[6,0,6,0,9,0,6,6,0,6],
]))