import time


def binary_search(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid][0] < target:
            left = mid + 1
        else:
            right = mid
    return arr[left][1]

n = int(input())
search_ids = [int(input()) for _ in range(n)]
filename = input()
with open(filename, 'r') as file:
    data = [tuple(int(c) for c in line.split()) for line in file]

t = time.time()
for i in search_ids:
    print(binary_search(data, i))
print(time.time() - t)