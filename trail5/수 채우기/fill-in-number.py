n = int(input())

# Please write your code here.

coins = [2, 5]

dp = [100000] * (n+1)
dp[0] = 0

for i in range(1, n+1):
    for j in coins:
        if i >= j:
            dp[i] = min(dp[i],dp[i-j]+1)

for i in range(1,n+1):
    if dp[i] == 100000:
        dp[i] = -1

print(dp[n])