import heapq
import sys
input = sys.stdin.readline


def my_print(heap):
    print(heapq.heappop(heap) if heap else 0)


heap = []
for _ in range(int(input())):
    n = int(input())
    if n != 0: heapq.heappush(heap, n)
    else: my_print(heap)