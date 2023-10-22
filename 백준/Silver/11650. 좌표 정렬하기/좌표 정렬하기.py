import sys
input = sys.stdin.readline


n = int(input())
coordinates = [tuple(map(int, input().split())) for _ in range(n)]
coordinates = sorted(coordinates, key=lambda c: (c[0], c[1]))
for x, y in coordinates: print(x, y)