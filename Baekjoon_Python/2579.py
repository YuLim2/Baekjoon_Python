import sys
input = sys.stdin.readline

n = int(input())
ls = [int(input()) for _ in range(n)]
dp = [0]*n

dp[0] = ls[0]
dp[1] = ls[0]+ls[1]
dp[2] = max(ls[1]+ls[2], ls[0]+ls[2])

for i in range(3, n):
    dp[i] = max(dp[i-3] + ls[i-1] + ls[i], dp[i-2] + ls[i])

print(dp[n - 1])