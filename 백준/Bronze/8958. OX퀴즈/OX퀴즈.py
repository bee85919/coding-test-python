def p_sum(n): return n*(n+1)//2

n = int(input())
for _ in range(n):
    sum = 0
    for i in input().split('X'):
        sum += p_sum(len(i))
    print(sum)