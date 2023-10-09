N = int(input())
NS= set(map(int, input().split()))
M = int(input())
ML = list(map(int, input().split()))

for i in range(len(ML)):
    print(1) if ML[i] in NS else print(0)