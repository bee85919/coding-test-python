import sys

def my_round(x): return int(x)+1 if x-int(x)>=0.5 else int(x)

input = sys.stdin.readline

n = int(input())
if n == 0: print(0); exit()

opinion = sorted([int(input()) for _ in range(n)])

exclude_num = my_round(n*0.15)
print(my_round(sum(opinion[exclude_num:n-exclude_num])/(n-2*exclude_num)))