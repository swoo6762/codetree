A, B = map(int, input().split())
num = 0
if A >= B:
    for i in range(B, A+1):
        if i % 5 == 0:
            num += i
else:
    for i in range(A, B+1):
        if i % 5 == 0:
            num += i

print(num)