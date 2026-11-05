arr = list(map(int, input().split()))

sum_even = 0
sum_three = 0
cnt_three = 0

for i in range(1, len(arr), 2):
    sum_even += arr[i]

for i in range(2, len(arr), 3):
    sum_three += arr[i]
    cnt_three += 1

print(f"{sum_even} {sum_three / cnt_three:.1f}")