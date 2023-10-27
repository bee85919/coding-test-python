import sys
input = sys.stdin.readline


from collections import deque


def dfs(v, graph, visit):
    dfs_visit(v, visit)
    for i in sorted(graph[v]):
        if not visit[i]:
            dfs(i, graph, visit)


def dfs_init(n, m):
    graph = graph_init(m)
    visit = visit_init(n)
    return graph, visit


def graph_init(m):
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    return graph


def visit_init(n): 
    return (n + 1)*[False]


def dfs_visit(v, visit):
    visit[v] = True
    print(v, end=' ')
    return visit


def bfs_init(v, visit):
    queue = deque([v])
    visit[v] = True
    return queue, visit


def bfs_print(v, queue):
    v = queue.popleft()
    print(v, end=' ')
    return v, queue


def bfs_visit(i, visit, queue):
    if not visit[i]:
        queue.append(i)
        visit[i] = True
    return visit, queue


def bfs(v, graph, visit):
    queue, visit = bfs_init(v, visit)
    while queue:
        v, queue = bfs_print(v, queue)
        for i in sorted(graph[v]):
            visit, queue = bfs_visit(i, visit, queue)


n, m, v = map(int, input().split())
graph, visit = dfs_init(n, m)
dfs(v, graph, visit)
print()


visit = visit_init(n)
bfs(v, graph, visit)