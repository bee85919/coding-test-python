import sys
input = sys.stdin.readline


def atm(times):
    ans, sum = 0, 0
    for t in times:
        sum += t
        ans += sum
    return ans


N = int(input())
times = sorted(list(map(int, input().split())))
print(atm(times))