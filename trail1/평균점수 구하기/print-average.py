score = list(map(float, input().split()))
num_sum = 0
cnt = 0
for i in score:
    num_sum += i
    cnt += 1
print(f"{num_sum/cnt:.1f}")