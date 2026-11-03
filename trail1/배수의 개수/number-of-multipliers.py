a, b = 0, 0

for i in range(10):
    T = int(input())
    if T % 3 == 0:
        a += 1
    if T % 5 == 0:
        b += 1

print(a, b)