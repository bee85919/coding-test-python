N, LIST = int(input()), []
for i in range(N):
    LIST.append(input().split())
LIST.sort(key=lambda x: int(x[0]))


for i in range(N):
    print(int(LIST[i][0]), LIST[i][1])