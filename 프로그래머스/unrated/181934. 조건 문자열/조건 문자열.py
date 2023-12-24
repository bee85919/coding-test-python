def solution(ineq, eq, n, m):
    if ineq == '>':
        if eq == '=':
            return 1 if n >= m else 0
        if eq == '!':
            return 1 if n > m else 0
    if ineq == '<':
        if eq == '=':
            return 1 if n <= m else 0
        if eq == '!':
            return 1 if n < m else 0