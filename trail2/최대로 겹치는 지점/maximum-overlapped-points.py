n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

cnt = [0] * 101

for a, b in segments:
    for i in range(a,b+1):
        cnt[i] += 1

ans = max(cnt)
print(ans)