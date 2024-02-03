def solution(arr, k):
    ans = []
    if k%2 == 1:
        for a in arr:
            ans.append(a*k)
    elif k%2 == 0:
        for a in arr:
            ans.append(a+k)
    return ans