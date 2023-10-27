import sys
from collections import deque


def ripped_tomato(tomato, n, m):
    dq = deque()
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 1:
                dq.append((i,j))
    return dq


def bfs_init(tomato, dq, n, m):
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    day = -1
    while dq:
        day += 1
        for _ in range(len(dq)):
            x, y = dq.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                bfs(tomato, dq, n, m, nx, ny)
    return tomato, day


def bfs(tomato, dq, n, m, nx, ny):
    if 0 <= nx < n and 0 <= ny < m:
        if tomato[nx][ny] == 0:
            tomato[nx][ny] = 1
            dq.append((nx, ny))
    return tomato


def check_tomato(tomato):
    for row in tomato:
        if 0 in row:
            print(-1)
            exit(0)


# input = sys.stdin.readline
m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]


dq = ripped_tomato(tomato, n, m)
tomato, day = bfs_init(tomato, dq, n, m)
check_tomato(tomato)


print(day)