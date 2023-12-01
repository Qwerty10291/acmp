n = int(input())

matrix = [[int(i) for i in input().split()] for _ in range(n)]
input()
colors = [int(i) for i in input().split()]
bad = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1 and colors[i] != colors[j]:
            matrix[j][i] = 0
            bad += 1

print(bad)