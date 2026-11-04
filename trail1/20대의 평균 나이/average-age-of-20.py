age_sum = 0
cnt = 0
while True:
    N = int(input())

    if N >= 30 or N <20:
        break
    else:
        cnt += 1
    age_sum += N

print(f"{age_sum/cnt:.2f}")