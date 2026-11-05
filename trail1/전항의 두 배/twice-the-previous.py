A, B = map(int, input().split())
arr = [A, B]

for i in range(1,9):
    arr.append(arr[i]+2*arr[i-1])

for i in arr:
    print(i,end=" ")