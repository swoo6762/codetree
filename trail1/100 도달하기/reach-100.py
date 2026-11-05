N = int(input())
arr=[1,N]
num = 0
while num<100:
    num = arr[-1] + arr[-2]
    arr.append(num)

for i in arr:
    print(i, end=" ")