cnt = 0
ans = 0
while cnt < 5:
    N = int(input())
    if N % 3 == 0:
        ans = 1
    else:
        ans = 0
        break
    cnt += 1
print(ans)
