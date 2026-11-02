A,B = map(int, input().split())

if A>=90 and B>=95:
    print(100000)
elif A>=90 and B>=90:
    print(50000)
else:
    print(0)