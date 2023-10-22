import sys
input=sys.stdin.readline


n, que = int(input()), []
for _ in range(n):
    q = input().split()
    if   q[0] == 'push' : que.append(q[1])
    elif q[0] == 'pop'  : print(que.pop(0) if que else -1)
    elif q[0] == 'size' : print(len(que))
    elif q[0] == 'empty': print(0 if que else 1)
    elif q[0] == 'front': print(que[0] if que else -1)
    elif q[0] == 'back' : print(que[-1] if que else -1)