import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)


dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]


def dfs(x, y, field, visit, m, n):
    visit[y][x] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if field[ny][nx] == 1 and not visit[ny][nx]:
                dfs(nx, ny, field, visit, m, n)


def create_field_and_visit(m, n):
    field = [[0] * m for _ in range(n)]
    visit = [[False] * m for _ in range(n)]
    return field, visit


def fill_field(k, field):
    for _ in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1
    return field


def count(m, n, field, visit):
    count = 0
    for i in range(m):
        for j in range(n):
            if field[j][i] == 1 and not visit[j][i]:
                dfs(i, j, field, visit, m, n)
                count += 1
    return count


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    field, visit = create_field_and_visit(m, n)
    field = fill_field(k, field)
    print(count(m, n, field, visit))