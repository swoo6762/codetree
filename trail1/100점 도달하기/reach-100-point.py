score = int(input())

while score <= 100:
    if score < 60:
        print("F", end = " ")
    elif score <70:
        print("D", end = " ")
    elif score <80:
        print("C", end=" ")
    elif score<90:
        print("B", end=" ")
    else:
        print("A", end=" ")
    score += 1 