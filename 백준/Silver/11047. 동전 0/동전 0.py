import sys
input = sys.stdin.readline


def greedy(k, c, cnt):
    x = k//c
    k -= c*x
    cnt += x
    return cnt, k


def cnt_coin(coin, k):
    cnt = 0
    for c in reversed(coin):
        if k == 0: break
        if c <= k: cnt, k = greedy(k, c, cnt)
    return cnt


n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
print(cnt_coin(coin, k))