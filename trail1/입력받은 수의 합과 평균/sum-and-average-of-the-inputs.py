N = int(input())
num_sum = 0
for i in range(N):
    T = int(input())
    num_sum += T

print(f"{num_sum} {num_sum/N:.1f}")