N = int(input())
num = 0
multiples = 0
while multiples < 2:
    num = num + N
    print(num, end= " ")
    if num % 5 == 0 and num != 0:
        multiples += 1