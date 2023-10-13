from collections import Counter


N = int(input())
CARD = list(map(int, input().split()))
M = int(input())
TARGET = list(map(int, input().split()))


CNT, ANS = Counter(CARD), []
for T in TARGET:
    ANS.append(str(CNT[T]))
print(" ".join(ANS))