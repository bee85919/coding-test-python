N = int(input())
for _ in range(N):
    n, i = map(int, input().split())
    P = list(map(int, input().split()))
    L = [(idx, p) for idx, p in enumerate(P)]
    
    cnt = 0
    while True:
        if L[0][1] == max(L, key=lambda x: x[1])[1]:
            cnt += 1
            if L[0][0] == i:
                print(cnt)
                break
            else:
                L.pop(0)
        else:
            L.append(L.pop(0))