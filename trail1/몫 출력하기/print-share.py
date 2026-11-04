ans = 0
while True:
    N = int(input())
    if N % 2 == 1:
        continue
    print(N//2)
    ans += 1

    if  ans >= 3:
        break
