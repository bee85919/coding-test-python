n = int(input())
lst = [input() for _ in range(n)]
lst = set(lst)
lst = sorted(list(lst), key=lambda x: (len(x), x))
for i in range(len(lst)): print(lst[i])