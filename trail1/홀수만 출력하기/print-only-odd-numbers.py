N = int(input())
a = 1
while a <= N:
    b = int(input())   
    if b % 2 == 1 and b % 3 == 0:
        print(b)
    a += 1 