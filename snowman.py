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
    elif len(arr[0]) == 1:
        arr = [[x for x in str(line[0])] for line in arr]

    length = len(arr[0])
    height = len(arr)

    def validate(point):
        y, x = point
        return (0 <= y < height) and (0 <= x < length)

    def explode(point):
        y, x = point
        
        valid2 = list(filter(validate, [(y - 1, x), (y, x + 1), (y + 1, x), (y, x - 1)]))
        arr[y][x] = "X"
        flattened = [x for line in arr for x in line]
        for p in valid2:
            py, px = p
            val = arr[py][px]
            if val == "9":
                explode(p)
                flattened = [x for line in arr for x in line]
                continue
            if flattened.count(val) > 1:
                arr[py][px] = "X"
        flattened = [x for line in arr for x in line]
        valid2 = []

    i = 0
    flattened = [x for line in arr for x in line] # removing this line causes runtime spike by 2+ seconds idk why or how

    size = length * height
    while True:
        p = 0
        while p < n:
            px = i % length
            py = i // length
            i += 1
            
            if i >= size:
                i -= size + 1
                continue
            if arr[py][px] != "X":
                p += 1

        val = arr[py][px]
        if val == "9":
            explode((py, px))
        else:
            flattened = [x for line in arr for x in line]
            if flattened.count(val) > 1:
                arr[py][px] = "X"
            else:
                break
    
    arr = []

    for item in ["0", "6"]:
        while flattened.count(item) > 1:
            i = "".join(flattened).rindex(item)
            #i = (len(flattened) - 1 - i)
            #arr[i // length][i % length] = "X"
            flattened[i] = "X"

    inside = tuple((flattened.index(item) // length, flattened.index(item) % length) if item in flattened else None for item in ["0", "6"])
    # tuple comprehension for the win lmao
    return inside

