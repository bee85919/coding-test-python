import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
ans = [-1]*n
sta = []


sta.append(0)
for i in range(1, n):
    while sta and A[sta[-1]] < A[i]: 
        ans[sta.pop()] = A[i]
    sta.append(i)


print(*ans)