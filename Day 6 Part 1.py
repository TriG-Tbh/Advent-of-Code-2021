import helper

with open(helper.nrml("day6.txt")) as f:
    contents = f.read()

contents = [int(x) for x in contents.split(",")]

def process(b):
    board = b.copy()
    i = 0
    length = len(board)
    while i < length:
        board[i] -= 1
        if board[i] == -1:
            board.append(9)
            board[i] = 6
        i += 1
        length = len(board)
    return board

for _ in range(80):
    contents = process(contents)

print(len(contents))