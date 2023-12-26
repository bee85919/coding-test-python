def solution(a, d, included):
    lst = [k for k, v in enumerate(included) if v == True]
    return sum([(a + d*i) for i in lst])