import sys
input = sys.stdin.readline


def my_fill(dict, i):
    a = input().rstrip()
    dict[i] = a
    dict[a] = i
    
    
def my_print(dict):
    a = input().rstrip()
    print(dict[int(a)] if a.isdigit() else dict[a])


n, m = map(int, input().rstrip().split())
dict = {}
for i in range(1, n+1): my_fill(dict, i)
for i in range(m): my_print(dict)