import sys
input = sys.stdin.readline


def cal(lst):
    ans = cal_init(lst)
    ans = cal_calc(ans, lst)
    return ans


def cal_init(lst):
    ans = sum(map(int, lst[0].split('+')))
    return ans


def cal_calc(ans, lst):
    for l in lst[1:]:
        ans -= sum(map(int, l.split('+')))
    return ans


lst = input().split('-')
ans = cal(lst)
print(ans)