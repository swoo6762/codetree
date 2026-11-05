N = int(input())
arr =list(map(int, input().split()))
even_arr = []
for i in range(N):
    if arr[i] % 2 == 0:
        even_arr.append(arr[i])
for i in even_arr:
    print(i,end= " ")