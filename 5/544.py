def count_ways_to_bottom(N):
    if N <= 1:
        return 1

    dp = [0] * (N + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[N]

N = int(input())
result = count_ways_to_bottom(N)
print(result)