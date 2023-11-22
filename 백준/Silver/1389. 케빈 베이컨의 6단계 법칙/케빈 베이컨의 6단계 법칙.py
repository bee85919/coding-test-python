n, m = map(int, input().split())


graph = [[9999] * (n + 1) for _ in range(n + 1)]


for i in range(1, n + 1):
    graph[i][i] = 0


for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1


for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


kevin_bacon = [sum(graph[i][1:]) for i in range(1, n + 1)]


min_value = min(kevin_bacon)
print(kevin_bacon.index(min_value) + 1)