def init():
    moves = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
    visit = set()
    edges = set()
    x, y = 0, 0
    visit.add((x, y))
    return moves, visit, edges, x, y


def count(x, y, a, cnt, moves, visit, edges):
    nx, ny = x + moves[a][0], y + moves[a][1]
    if (nx, ny) in visit:
        if ((x, y), (nx, ny)) not in edges and ((nx, ny), (x, y)) not in edges:
            cnt += 1
    else:
        visit.add((nx, ny))
    return nx, ny, cnt, visit


def update(x, y, nx, ny, edges):
    edges.add(((x, y), (nx, ny)))
    edges.add(((nx, ny), (x, y)))
    x, y = nx, ny
    return x, y, edges


def solution(arrow):
    moves, visit, edges, x, y = init()
    cnt = 0
    for a in arrow:
        for _ in range(2):
            nx, ny, cnt, visit = count(x, y, a, cnt, moves, visit, edges)                        
            x, y, edges = update(x, y, nx, ny, edges)
    return cnt