arr = list(map(int, input().split()))
num = 0
cnt = 0
for i in range(len(arr)):
    if arr[i] % 2 == 0 and arr[i] != 0:
        num += arr[i]
        cnt += 1
    elif arr[i] == 0:
        break
print(f"{cnt} {num}")