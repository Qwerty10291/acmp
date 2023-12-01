def count_palindrome_ways(S):
    N = len(S)
    # dp[i][j] - количество способов получить палиндром из подстроки S[i:j+1]
    dp = [[0] * N for _ in range(N)]

    for i in range(N):
        dp[i][i] = 1

    for i in range(N-1, -1, -1):
        for j in range(i+1, N):
            if S[i] == S[j]:
                dp[i][j] = dp[i+1][j] + dp[i][j-1] + 1
            else:
                dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]

    return dp[0][N-1]

print(count_palindrome_ways(input().lower()))
