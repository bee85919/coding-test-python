import sys
input = sys.stdin.readline


n = int(input())
n_list = [input().split() for _ in range(n)]
n_list = sorted(n_list, key=lambda x: int(x[0]))
for i in range(n): print(int(n_list[i][0]), n_list[i][1])