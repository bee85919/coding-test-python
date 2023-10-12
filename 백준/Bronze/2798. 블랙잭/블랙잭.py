N, NUM = map(int, input().split())
L = list(map(int, input().split()))


MAX = 0
ANS = 0
FOUND = False
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            SUM = L[i] + L[j] + L[k]
            if SUM == NUM:
                print(SUM)
                FOUND = True
                break
            if SUM > NUM:
                continue
            else:
                ANS = SUM
                if MAX < ANS:
                    MAX = ANS
        else:
            continue
        break
    else:
        continue
    break


if not FOUND:
    print(MAX)