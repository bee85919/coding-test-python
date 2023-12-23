def solution(n):
    if n%2 == 1: return sum(int for int in range(1, n+1, 2))
    if n%2 == 0: return sum(int**2 for int in range(2, n+1, 2))