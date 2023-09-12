import heapq

stdin = open(0)
n = int(stdin.readline()[:-1].split()[0])
matrix = []
for i in range(n):
    matrix.append([int(c) for c in stdin.readline()[:-1].split()])
m = len(matrix[0])


def dijkstra(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    distances = [[float('inf')] * cols for _ in range(rows)]

    start = (0, 0)
    distances[start[0]][start[1]] = grid[start[0]][start[1]]

    min_heap = [(grid[start[0]][start[1]], start)]

    while min_heap:
        dist, current = heapq.heappop(min_heap)

        if current == (rows - 1, cols - 1):
            return dist

        for dr, dc in directions:
            r, c = current[0] + dr, current[1] + dc

            if 0 <= r < rows and 0 <= c < cols:
                new_dist = dist + grid[r][c]

                if new_dist < distances[r][c]:
                    distances[r][c] = new_dist
                    heapq.heappush(min_heap, (new_dist, (r, c)))

    return -1

print(dijkstra(matrix))