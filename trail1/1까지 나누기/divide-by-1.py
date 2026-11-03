N = int(input())
cnt = 0
num = 1
while N > 1:
    N //= num
    cnt += 1
    num += 1

print(cnt)