arr = list(map(int, input().split()))

result = []

for n in arr:
    if n == 0:
        break
    result.append(n)

for i in range(len(result) - 1, -1, -1):
    print(result[i], end=" ")
