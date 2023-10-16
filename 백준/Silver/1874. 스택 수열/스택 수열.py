N = int(input())
L = [int(input()) for _ in range(N)]

sta, ans, cur = [], [], 0

for i in L:
    while cur < i:
        cur += 1
        sta.append(cur)
        ans.append('+')
    if sta[-1] == i:
        sta.pop()
        ans.append('-')
    else:
        print('NO')
        exit(0)
else:
    for a in ans:
        print(a)