n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.

cnt = [0]* 10000
point = 1000

for i in range(n):
    if dir[i] == "R":
        for j in range(point, point + x[i]):
            cnt[j] += 1
        point += x[i]
    
    else:
        for j in range(point-x[i], point):
            cnt[j] += 1
        point -= x[i]

ans = 0
for i in range(10000):
    if cnt[i] >= 2:
        ans+=1

print(ans)
        