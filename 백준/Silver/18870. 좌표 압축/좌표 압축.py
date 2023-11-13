import sys
input = sys.stdin.readline


n = int(input())
xys = list(map(int, input().split()))
sort_xys = sorted(set(xys))
dict_xys = {xy: i for i, xy in enumerate(sort_xys)}
ans = [dict_xys[xy] for xy in xys]
print(' '.join(str(a) for a in ans))