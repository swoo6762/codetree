N = int(input())
cnt = 0
for i in range(1,N):
    if N%i == 0:
        cnt += i

if cnt == N:
    print("P")
else:
    print("N")