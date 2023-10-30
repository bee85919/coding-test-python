def dfs(x, y, arr, vst, N):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    vst[x][y] = True
    cnt = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if arr[nx][ny] == 1 and not vst[nx][ny]:
                cnt += dfs(nx, ny, arr, vst, N)
    return cnt


n = int(input())
arr = [list(map(int, input().strip())) for _ in range(n)]
vst = [n*[False] for _ in range(n)]


ans = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and not vst[i][j]:
            ans.append(dfs(i, j, arr, vst, n))


ans.sort()
print(len(ans))
for r in ans: print(r)