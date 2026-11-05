N = int(input())
score_pass = 0

for i in range(N):
    score = list(map(int, input().split()))
    score_sum = 0
    score_num = 0
    for j in score:
        score_sum += j
        score_num += 1
    if (score_sum / score_num) >= 60:
        print("pass")
        score_pass += 1
    else:
        print("fail")
print(score_pass)
