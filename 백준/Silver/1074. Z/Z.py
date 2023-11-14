import sys
input = sys.stdin.readline
sys.setrecursionlimit(9999)


def z_search(n, r, c):

    if n == 0: return 0

    m = 2**(n-1)

    if r < m and c < m:
        return z_search(n-1, r, c)
    
    if r < m and c >= m:
        return m*m + z_search(n-1, r, c-m)
    
    if r >= m and c < m:
        return 2*m*m + z_search(n-1, r-m, c)
    
    return 3*m*m + z_search(n-1, r-m, c-m)


n, r, c = map(int, input().split())
print(z_search(n, r, c))