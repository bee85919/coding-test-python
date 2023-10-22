from collections import Counter


n = int(input())
card = list(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))


cnt = Counter(card)
ans = [str(cnt[t]) for t in target]
print(" ".join(ans))