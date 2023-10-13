import sys

N, K = map(int, sys.stdin.readline().split())
i, ANS, LIST = 0, [], [n for n in range(1, N+1)]
while LIST:
    i += K-1
    if i >= len(LIST):
        i %= len(LIST)
    ANS.append(str(LIST.pop(i)))
print('<', ', '.join(ANS), '>', sep='')