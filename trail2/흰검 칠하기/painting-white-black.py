n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.

cnt = [0] * 1000001
white = [0] * 1000001
black = [0] * 1000001

point = 500000

for i in range(n):
    if dir[i] == "R":
        for j in range(point, point + x[i]):
            black[j] += 1
            cnt[j] = 1

        point += x[i] - 1
    else:
        for j in range(point - x[i] + 1, point + 1):
            white[j] += 1
            cnt[j] = 2

        point -= x[i] - 1

ans_white = 0
ans_black = 0
ans_gray = 0

for i in range(1000001):
    if white[i] >= 2 and black[i] >= 2:
        ans_gray += 1
    elif cnt[i] == 1:
        ans_black += 1
    elif cnt[i] == 2:
        ans_white += 1

print(ans_white, ans_black, ans_gray)