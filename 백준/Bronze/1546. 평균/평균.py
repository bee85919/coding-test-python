M = int(input())
score = input().split()
score = [int(s) for s in score]
max_score = max(score)
for i in range(M):
    score[i] = score[i]/max_score*100
print(sum(score)/M)