N = int(input())
score = list(map(float, input().split()))
num_sum = 0
cnt = 0
for i in score:
    num_sum += i
    cnt += 1

if num_sum / cnt >= 4.0:
    print(f"{num_sum / cnt:.1f}")
    print("Perfect")
elif num_sum / cnt >= 3.0:
    print(f"{num_sum / cnt:.1f}")
    print("Good")
else:
    print(f"{num_sum / cnt:.1f}")
    print("Poor")