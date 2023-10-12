import sys
input=sys.stdin.readline


N = int(input())
Q = []
for _ in range(N):
    q = input().split()
    if q[0] == 'push': Q.append(q[1])
    elif q[0] == 'pop': print(Q.pop(0) if Q else -1)
    elif q[0] == 'size': print(len(Q))
    elif q[0] == 'empty': print(0 if Q else 1)
    elif q[0] == 'front': print(Q[0] if Q else -1)
    elif q[0] == 'back': print(Q[-1] if Q else -1)