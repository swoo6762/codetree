n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.

cnt = [0] * 10000
point = 5000

for i in range(n):
    if dir[i] == "R":
        for j in range(point, point + x[i]):
            cnt[j] = 1
        point += x[i] - 1
    else:
        for j in range(point - x[i] + 1, point + 1):
            cnt[j] = 2
        point -= x[i] - 1

black = 0
white = 0

for i in range(10000):
    if cnt[i] == 1:
        black += 1
    elif cnt[i] == 2:
        white += 1
    else:
        continue

print(white, black)