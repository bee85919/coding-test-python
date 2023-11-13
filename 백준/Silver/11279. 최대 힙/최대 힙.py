import sys
input = sys.stdin.readline


import heapq


def my_print(heap):
    print(-1*heapq.heappop(heap) if heap else 0)


heap = []
for _ in range(int(input())):
    n = -1*int(input())
    if n != 0: heapq.heappush(heap, n)
    else: my_print(heap)