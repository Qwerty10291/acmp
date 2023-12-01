
def colorize(m, x, y):
    stack = [(x, y)]
    while len(stack):
        x, y = stack.pop()
        if (y < 0 or y >= len(m)) or (x < 0 or x >= len(m[y])) or m[y][x] != 0:
            continue
        m[y][x] = 2
        stack.append((x, y - 1))
        stack.append((x - 1, y))
        stack.append((x + 1, y))
        stack.append((x, y + 1))

n, m = (int(i) for i in input().split())
matrix = [[0 if j == "#" else 1 for j in input()] for _ in range(n)]

pieces = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            colorize(matrix, j, i)
            pieces += 1
print(pieces)