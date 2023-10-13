def F(n):
    if n == 0: return 1
    return F(n-1)*n

n, k = map(int, input().split())
print(F(n) // (F(k)*F(n-k)))
