def solution(a, b, c):
    n = len(set([a, b, c]))
    return (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3) if n == 1 \
    else (a+b+c)*(a**2+b**2+c**2) if n == 2 \
    else (a+b+c)