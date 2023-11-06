import sys
input = sys.stdin.readline
sys.setrecursionlimit(9999)


def graph_init(n):
    return [[] for _ in range(n+1)]


def graph_fill(graph, m):
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    return graph


def visit_init():
    return [False for _ in range(n+1)]


def dfs_cnt(graph, visit, n):
    cnt = 0
    for i in range(1, n+1):
        if not visit[i]:
            dfs(graph, visit, i)
            cnt += 1
    return cnt


def dfs(graph, visit, i):
    visit[i] = True
    for j in graph[i]:
        if not visit[j]:
            dfs(graph, visit, j)


n, m = map(int, input().split())
graph = graph_init(n)
graph = graph_fill(graph, m)
visit = visit_init()
cnt = dfs_cnt(graph, visit, n)
print(cnt)