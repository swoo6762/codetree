n = int(input())

# Please write your code here.

dp = [0] * (n+1)
dp[0], dp[1], dp[2] = 0, 0, 1
if n >= 3:
    dp[3] = 1
for i in range(4, n+1):
    dp[i] = dp[i-2] + dp[i-3]


ans = dp[n] % 10007
print(ans)
