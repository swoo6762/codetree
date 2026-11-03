num_sum = 0
cnt = 0

for i in range(10):
    T = int(input())
    if 0 <= T <= 200:
        num_sum += T
        cnt += 1

print(f'{num_sum} {num_sum/cnt:.1f}')