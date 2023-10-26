import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)


dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]


def dfs(x, y, field, visit, m, n):
    visit[x][y] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if field[nx][ny] == 1 and not visit[nx][ny]:
                dfs(nx, ny, field, visit, m, n)


def create_field_and_visit(m, n):
    field = [[0] * n for _ in range(m)]
    visit = [[False] * n for _ in range(m)]
    return field, visit


def fill_field(k, field):
    for _ in range(k):
        x, y = map(int, input().split())
        field[x][y] = 1
    return field


def cnt(m, n, field, visit):    
    count = 0
    for i in range(m):
        for j in range(n):
            if field[i][j] == 1 and not visit[i][j]:
                dfs(i, j, field, visit, m, n)
                count += 1
    return count


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    field, visit = create_field_and_visit(m, n)
    field = fill_field(k, field)
    print(cnt(m, n, field, visit))