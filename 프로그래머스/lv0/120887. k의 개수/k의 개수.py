def solution(i, j, k):
    return ''.join(map(str, range(i, j+1))).count(str(k))