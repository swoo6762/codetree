arr = list(map(int, input().split()))
ans = []
for i in arr:
    if i % 2 == 1:
        ans.append(i+3)
    elif i == 0:
        break
    else:
        ans.append(i//2)

for i in ans:
    print(i,end=" ")