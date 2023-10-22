import sys


n, k = map(int, sys.stdin.readline().split())
i, ans, lst = 0, [], [n for n in range(1, n+1)]
while lst:
    i += k-1
    if i >= len(lst): i %= len(lst)
    ans.append(str(lst.pop(i)))
print('<', ', '.join(ans), '>', sep='')