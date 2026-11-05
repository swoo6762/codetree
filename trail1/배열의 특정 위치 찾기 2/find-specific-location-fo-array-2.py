arr = list(map(int, input().split()))
even_sum = 0
odd_sum = 0

for i in range (0,len(arr),2):
    odd_sum += arr[i]
for j in range (1,len(arr),2):
    even_sum += arr[j]

print(abs(even_sum - odd_sum))