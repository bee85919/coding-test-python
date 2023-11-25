def get_pre_sum():
    s = 0
    pre_sum = [0]*(n+1)
    for i in range(n):
        s += arr[i]
        pre_sum[i+1] = s
    return pre_sum


def get_max_sum():
    max_sum = -int(1e9)
    for i in range(k, n+1):
        max_sum = max(max_sum, pre_sum[i]-pre_sum[i-k])
    return max_sum


n,k = map(int, input().split())
arr = list(map(int, input().split()))
pre_sum = get_pre_sum()
max_sum = get_max_sum()
print(max_sum)