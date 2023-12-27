def solution(a, b, c):
    ans = 0
    if a != b and b != c and c != a:
        ans = (a+b+c)
    elif a == b == c:
        ans = (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
    else: 
        ans = (a+b+c)*(a**2+b**2+c**2)
    return ans