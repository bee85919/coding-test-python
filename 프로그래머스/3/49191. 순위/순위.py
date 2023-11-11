def graph_init(n):
    return [[False for _ in range(n)] for _ in range(n)]


def graph_update(graph, results):
    for winner, loser in results:
        graph[winner-1][loser-1] = True
    return graph


def alg_fw(graph, n):  # Floyd Warshall Algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = True
    return graph


def graph_cnt(graph, n):
    ans = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if graph[i][j] or graph[j][i]:
                cnt += 1
        if cnt == n-1:
            ans += 1
    return ans


def solution(n, results):
    graph = graph_init(n)
    graph = graph_update(graph, results)
    graph = alg_fw(graph, n)
    return graph_cnt(graph, n)