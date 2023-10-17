n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
sorted_points = sorted(points, key=lambda x: (x[1], x[0]))
for point in sorted_points:
    print(point[0], point[1])