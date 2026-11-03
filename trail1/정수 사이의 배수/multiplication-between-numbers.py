A, B = map(int, input().split())
num = 0
count = 0
for i in range(A,B+1):
    if i%5 == 0 or i%7 == 0:
        num += i
        count += 1

print(f"{num} {num/count:.1f}" )

