N = int(input())

stairs = [0] + [int(input()) for _ in range(N)]

dp = [0 for i in range(N+1)]

dp[1] = stairs[1]

if N == 1:
    print(dp[1])

else:

    dp[2] = stairs[1] + stairs[2]

    for i in range(3, N+1):
        dp[i] = max(dp[i-2], dp[i-3] + stairs[i-1]) + stairs[i]

    print(dp[-1])