N, M = map(int, input().split())
arr =[N, M]

for i in range(2, 10):
    arr.append((arr[i-1]+arr[i-2])%10)

for i in arr:
    print(i,end=" ")