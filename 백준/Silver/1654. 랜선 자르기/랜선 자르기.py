K, N = map(int, input().split())
L = [int(input()) for _ in range(K)]

S, E = 1, max(L)
while S <= E:
    M = (S+E) // 2
    T = sum(l // M for l in L)
    if T < N:
        E = M - 1
    else:
        S = M + 1

print(E)