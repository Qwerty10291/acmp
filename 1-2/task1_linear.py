import time


n = int(input())
search_ids = [int(input()) for _ in range(n)]
filename = input()
with open(filename, 'r') as file:
    data = [tuple(int(c) for c in line.split()) for line in file]

t = time.time()
for i in search_ids:
    for r in data:
        if r[0] == i:
            print(r[1])
print(time.time() - t)