import sys
input = sys.stdin.readline


from collections import deque


def bfs(n, k):
    queue, visit = bfs_init(n)
    while queue:
        now = queue.popleft()        

        caught = now == k
        if caught:
            return visit[now] - 1

        for m in move(now):
            queue, visit = visited(queue, visit, now, m)


def bfs_init(n):
    queue = deque([n])
    visit = 100001*[0]
    visit[n] = 1
    return queue, visit


def move(now): return [now-1, now+1, 2*now]


def visited(queue, visit, now, m):
    if 0 <= m <= 100000 and not visit[m]:
        visit[m] = visit[now] + 1
        queue.append(m)
    return queue, visit


n, k = map(int, input().split())
print(bfs(n, k))