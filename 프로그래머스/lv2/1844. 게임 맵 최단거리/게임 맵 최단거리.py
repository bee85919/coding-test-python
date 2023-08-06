from collections import deque

def solution(maps):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    n = len(maps)
    m = len(maps[0])
    
    distance = [m*[-1]for _ in range(n)]
    distance[0][0] = 1

    queue = deque()
    queue.append((0, 0))
    
    # BFS
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            
            if maps[nx][ny] == 0: continue
            
            if distance[nx][ny] == -1:
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))
    
    return distance[n-1][m-1]