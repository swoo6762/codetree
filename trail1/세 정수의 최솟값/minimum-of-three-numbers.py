a,b,c = map(int, input().split())

if a <= b:
    min_num = a
else:
    min_num = b

if min_num < c:
    pass
else:
    min_num = c

print(min_num)