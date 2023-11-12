from collections import deque


def graph_init(n, vertex):
    graph = [[] for _ in range(n+1)]
    for v1, v2 in vertex:
        graph[v1].append(v2)
        graph[v2].append(v1)
    return graph


def dist_init(n):
    dist = [0]*(n+1)
    dist[1] = 1
    return dist


def get_dist(queue, graph, dist):
    current = queue.popleft()
    for next in graph[current]:
        if dist[next] == 0:
            dist[next] = dist[current] + 1
            queue.append(next)
    return queue, graph, dist


def solution(n, vertex):
    graph = graph_init(n, vertex)
    dist = dist_init(n)
    queue = deque([1])
    while queue:
        queue, graph, dist = get_dist(queue, graph, dist)
    return dist.count(max(dist))