# Run as:
# snowman(n, arr)
import numpy as np # unexpected rapid increase???

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
        flattened = np.array([str(x) for line in arr for x in line])
        length = len(arr[0])
        height = len(arr)
    elif len(arr[0]) == 1:
        flattened = np.array([x for line in arr for x in str(line[0])])
        height = len(arr)
        length = len(arr[0][0])
    else:
        flattened = np.array([x for line in arr for x in line])
        length = len(arr[0])
        height = len(arr)

    arr = []

    
    def explode(point):
        y, x = point
        
        flattened[(y * length) + x] = "X"
        for p in filter(lambda x: (0 <= x[0] < height) and (0 <= x[1] < length), [(y - 1, x), (y, x + 1), (y + 1, x), (y, x - 1)]):
            index = (p[0] * length) + p[1]
            val = flattened[index]
            if val == "9":
                explode(p)
                continue
            if np.count_nonzero(flattened == val) > 1:
                flattened[index] = "X"

    i = 0
    
    size = length * height
    while True:
        p = 0
        while p < n:
            if i == size: 
                i -= size + 1
                continue
            if flattened[i] != "X":
                p += 1
            if p < n:
                i += 1

        val = flattened[i]
        if val == "9":
            explode((i // length, i % length))
            continue
        if np.count_nonzero(flattened == val) > 1:
            flattened[i] = "X"
            continue
        break
    

    inside = tuple((np.nonzero(flattened == item)[0][0] // length, np.nonzero(flattened == item)[0][0] % length) if item in flattened else None for item in ["0", "6"])
    # tuple comprehension for the win lmao
    
    flattened = []
    
    return inside