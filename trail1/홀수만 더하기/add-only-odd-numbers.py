N = int(input())
cnt = 0
for i in range(N):
    T = int(input())
    if T % 2 == 1 and T % 3 == 0:
        cnt += T

print(cnt)