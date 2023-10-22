import sys
input=sys.stdin.readline


n = int(input())
lst = [int(input()) for _ in range(n)]
for l in sorted(lst): print(l)