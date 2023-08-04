def solution(n, com):
    link = n*[0]

    def dfs(i):
        if link[i] == 0:
            link[i] = 1            
            for j in range(n):
                if com[i][j] == 1 and link[j] == 0: dfs(j)

    count = 0
    for i in range(n):
        if link[i] == 0:
            dfs(i)
            count += 1

    return count