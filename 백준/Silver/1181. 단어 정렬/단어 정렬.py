N = int(input())
List = []
for _ in range(N):
    List.append(input())

List = sorted(list(set(List)), key=lambda x: (len(x), x))
for i in range(len(List)):
    print(List[i])