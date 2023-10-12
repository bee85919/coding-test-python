n = int(input())
for _ in range(n):
    ans=0
    for s in input():
        if s == '(':
            ans += 1
        elif s == ')':
            ans -= 1
        if ans < 0:
            print('NO')
            break
    else:
        if ans == 0:
            print('YES')
        else:
            print('NO')