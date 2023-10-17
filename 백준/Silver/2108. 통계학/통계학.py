import sys
from collections import Counter

n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(n)]

sorted_nums = sorted(nums)
mc = Counter(sorted_nums).most_common()

mean = round(sum(nums)/n)
median = sorted_nums[n//2]
mode = mc[1][0] if len(mc) > 1 and mc[0][1] == mc[1][1] else mc[0][0]
range_val = sorted_nums[-1] - sorted_nums[0]

print(mean)
print(median)
print(mode)
print(range_val)