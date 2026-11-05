arr = list(map(int, input().split()))
cnt = 0
num_sum = 0
for i in range(len(arr)):
    if arr[i] != 0:
        cnt += 1
    else:
        break
for i in range(cnt):
    num_sum += arr[i]

print(f"{num_sum} {num_sum/cnt:.1f}")
