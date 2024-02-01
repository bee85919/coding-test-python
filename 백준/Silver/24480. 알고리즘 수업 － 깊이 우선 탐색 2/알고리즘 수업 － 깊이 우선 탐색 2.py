import sys


# sys.stdin.readline
input = sys.stdin.readline


# setrecursionlimit
sys.setrecursionlimit(99999999)


# dfs
def dfs(v):
    # global
    global cnt
    # check visited
    visited[v] = True
    # update cnt
    ans[v] = cnt
    # 내림 차순
    graph[v].sort(reverse=True)
    # 방문
    for i in graph[v]:
        # 방문 하지 않았다면
        if not visited[i]:
            cnt += 1
            dfs(i)
        # 방문 했다면 None


n, m, r = map(int, input().split())


# initialization
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
ans = [0] * (n+1)
cnt = 1


# fill graph
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


# dfs
dfs(r)


# print
for val in ans[1:]:
    print(val)