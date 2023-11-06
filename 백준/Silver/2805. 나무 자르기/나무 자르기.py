# import sys
# input = sys.stdin.readline


def bs(tree, m, s, e):
    while s <= e:
        mid = (s+e)//2
        psum = sum(t-mid if t>mid else 0 for t in tree)
        s, e = bs_calc(psum, mid, m, s, e)
    return e


def bs_calc(psum, mid, m, s, e):
    if psum >= m: 
        return mid+1, e
    else: 
        return s, mid-1
    

n, m = map(int, input().split())
tree = list(map(int, input().split()))
hght = bs(tree, m, 0, max(tree))
print(hght)