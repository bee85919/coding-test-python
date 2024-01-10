def backtracking():
    if len(li) == m:
        print(" ".join(map(str, li)))
        return
    for i in range(1, n+1):
        if i not in li:
            li.append(i)
            backtracking()
            li.pop()


n, m = map(int,input().split())  # 4 2
li = []
backtracking()