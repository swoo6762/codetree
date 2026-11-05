arr = list(map(int, input().split()))
cnt = 0
num = 0
for i in arr:
    if i >= 250:
        break
    num += i
    cnt += 1
    
print(f"{num} {num/cnt:.1f}")