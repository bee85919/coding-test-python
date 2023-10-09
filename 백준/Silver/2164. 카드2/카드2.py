from collections import deque

N = int(input())
deque = deque([n for n in range(1, N+1)])

for _ in range(N-1):
    deque.popleft()
    num = deque.popleft()
    deque.append(num)

print(deque[0])