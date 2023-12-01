n, m = (int(i) for i in input().split())

def colorize(m, x, y):
    if (y < 0 or y >= len(m)) or (x < 0 or x >= len(m[y])) or m[y][x] != 0:
        return
    m[y][x] = 2
    colorize(m, x, y - 1)
    colorize(m, x - 1, y)
    colorize(m, x + 1, y)
    colorize(m, x, y + 1)

matrix = [[int(j) for j in input().split()] for _ in range(n)]
pieces = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            colorize(matrix, j, i)
            pieces += 1
print(pieces)