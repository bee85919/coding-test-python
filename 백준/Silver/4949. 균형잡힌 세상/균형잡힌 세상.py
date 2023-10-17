import sys

def CHECK(string):
    S = []                 # S = Stack
    B = {'(':')', '[':']'} # B = Bracket
    for s in string:
        if s in B:
            S.append(s)
        elif s in B.values():
            if not S or B[S[-1]] != s:
                return False
            S.pop()
    return not S

while True:
    L = sys.stdin.readline().rstrip()
    if L == '.':
        break
    print("yes" if CHECK(L) else "no")