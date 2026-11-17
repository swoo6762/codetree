n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

cnt = [0] * 201

for a, b in segments:
    for i in range(a+100,b+100):
        cnt[i] += 1

ans = max(cnt)

print(ans)