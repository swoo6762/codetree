A = input()
arr = A.split()
per1 = arr[0]
per1_tem = int(arr[1])
A = input()
arr = A.split()
per2 = arr[0]
per2_tem = int(arr[1])
A = input()
arr = A.split()
per3 = arr[0]
per3_tem = int(arr[1])

A = 0
B = 0
C = 0
D = 0
if per1 == "Y" and per1_tem >=37:
    A += 1
elif per1 == "N" and per1_tem >=37:
    B += 1
elif per1 == "Y" and per1_tem < 37:
    C += 1
else:
    D += 1

if per2 == "Y" and per2_tem >=37:
    A += 1
elif per2 == "N" and per2_tem >=37:
    B += 1
elif per2 == "Y" and per2_tem < 37:
    C += 1
else:
    D += 1

if per3 == "Y" and per3_tem >=37:
    A += 1
elif per3 == "N" and per3_tem >=37:
    B += 1
elif per3 == "Y" and per3_tem < 37:
    C += 1
else:
    D += 1


if A >= 2:
    print("E")
else:
    print("N")
