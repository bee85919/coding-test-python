def solution(arr, k):
    ans = []
    for a in arr:
        if k%2 == 1:
            ans.append(a*k)
        elif k%2 == 0:
            ans.append(a+k)
    return ans