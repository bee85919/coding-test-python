import sys
input = sys.stdin.readline


def mysum(nums):
    sums = [0]
    s = 0
    for i in range(0, len(nums)):
        s += nums[i]
        sums.append(s)
    return sums


def diff(sums, i, j):
    return sums[j]-sums[i-1]


n, m = input().strip().split()
nums = list(map(int, input().strip().split()))
sums = mysum(nums)
for _ in range(int(m)):
    i, j = map(int, input().strip().split())
    print(diff(sums, i, j))