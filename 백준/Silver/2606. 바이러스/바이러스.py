import sys
input = sys.stdin.readline


def graph(lst, m):
    for _ in range(m):
        a, b = map(int, input().split())
        lst[a].append(b)
        lst[b].append(a)
    return lst


def dfs(i, vst, lst):
    vst[i] = True
    for l in lst[i]:
        if not vst[l]:
            dfs(l, vst, lst)
    return vst


n = int(input())
m = int(input())


lst = [[] for _ in range(n+1)]
vst = (n+1)*[False]


lst = graph(lst, m)
vst = dfs(1, vst, lst)


print(sum(vst)-1)