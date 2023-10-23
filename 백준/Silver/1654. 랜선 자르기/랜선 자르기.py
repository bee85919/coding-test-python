import sys
input = sys.stdin.readline


def get_mid(shrt, long): return (shrt + long) // 2
def cnt_lan(lans, mid): return sum(l // mid for l in lans)
def cal_mid(long, shrt, cnt, mid, n): return (mid-1, shrt) if cnt<n else (long, mid+1)


k, n = map(int, input().split())
lans = [int(input()) for _ in range(k)]
shrt, long = 1, max(lans)
while shrt <= long:
    mid = get_mid(shrt, long)
    cnt = cnt_lan(lans, mid)
    long, shrt = cal_mid(long, shrt, cnt, mid, n)
print(long)