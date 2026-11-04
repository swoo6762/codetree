A, B = map(int, input().split())
ans = 0
for i in range(A,B+1):
    if 1920 % i == 0 and 2880 % i == 0:
        ans = 1

print(ans)