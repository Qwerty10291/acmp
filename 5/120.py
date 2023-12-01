def min_cost_path(cost):
    N = len(cost)
    M = len(cost[0])

    # Создаем таблицу dp и заполняем ее значениями из первой строки и первого столбца
    dp = [[0] * M for _ in range(N)]
    dp[0][0] = cost[0][0]

    # Заполняем первую строку
    for j in range(1, M):
        dp[0][j] = dp[0][j-1] + cost[0][j]

    # Заполняем первый столбец
    for i in range(1, N):
        dp[i][0] = dp[i-1][0] + cost[i][0]

    # Заполняем остальные ячейки
    for i in range(1, N):
        for j in range(1, M):
            dp[i][j] = cost[i][j] + min(dp[i-1][j], dp[i][j-1])

    return dp[N-1][M-1]


n = int(input().split()[0])
matrix = [[int(i) for i in input().split()] for _ in range(n)]
print(min_cost_path(matrix))