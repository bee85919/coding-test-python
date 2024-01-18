def solution(a, b):
    c1 = (a % 2 == 1) and (b % 2 == 1)
    c2 = (a % 2 == 1) or (b % 2 == 1)
    ans = a**2 + b**2 if c1 else 2*(a + b) if c2 else abs(a-b)
    return ans