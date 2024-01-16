def solution(li):
    n1 = li[-1]
    n2 = li[-2]
    n = n1 - n2 if n1 > n2 else n1 * 2
    li.append(n)
    return li