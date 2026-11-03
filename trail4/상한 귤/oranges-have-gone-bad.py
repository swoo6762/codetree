n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

dp = [[n**n] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            dp[i][j] = 0
        elif grid[i][j] == 0:
            dp[i][j] = -1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while True:
    changed = False

    for i in range(n):
        for j in range(n):

            if grid[i][j] == 0:
                continue

            for d in range(4):
                ni = i + dx[d]
                nj = j + dy[d]

                if 0 <= ni < n and 0 <= nj < n:
                    if grid[ni][nj] == 0:
                        continue

                    if dp[ni][nj] != -1:
                        if dp[i][j] > dp[ni][nj] + 1:
                            dp[i][j] = dp[ni][nj] + 1
                            changed = True

    if not changed:
        break

for i in range(n):
    for j in range(n):
        if grid[i][j] == 0:
            print(-1, end=" ")
        elif dp[i][j] == n**n:
            print(-2, end=" ")
        else:
            print(dp[i][j], end=" ")
    print()