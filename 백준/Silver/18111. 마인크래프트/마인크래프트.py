import sys


input = input = sys.stdin.readline
N, M, B = map(int, input().split())
TERRAIN = [list(map(int, input().split())) for _ in range(N)]


height_dict = {}
for i in range(N):
    for j in range(M):
        if TERRAIN[i][j] not in height_dict:
            height_dict[TERRAIN[i][j]] = 0
        height_dict[TERRAIN[i][j]] += 1

        
ans, idx = float('inf'), -1


for h in range(257):
    if h not in height_dict:
        height_dict[h] = 0
    min_t = max_t = 0
    for key in height_dict:
        if key < h:
            min_t += (h - key) * height_dict[key]
        elif key > h:
            max_t += (key - h) * height_dict[key]
    if min_t <= max_t + B:
        time = min_t + 2*max_t
        if time <= ans:
            ans, idx = time, h

            
print(ans, idx)