import sys
input = sys.stdin.readline


def make_lst(n):
    lst = [list(map(int, input().split())) for _ in range(n)]
    lst = sorted(lst, key=lambda x: (x[1], x[0]))
    return lst


def cnt_lst(n, lst, cnt, end):
    for i in range(1, n):
        if lst[i][0] >= end:
            cnt += 1
            end = lst[i][1]
    return cnt, end


n = int(input())
lst = make_lst(n)
cnt, end = 1, lst[0][1]
cnt, end = cnt_lst(n, lst, cnt, end)


print(cnt)