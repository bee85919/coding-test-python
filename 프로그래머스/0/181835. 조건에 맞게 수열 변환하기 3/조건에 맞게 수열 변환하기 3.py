def solution(arr, k):
    if k%2 == 1:
        ans = [k*a for a in arr]
    elif k%2 == 0:
        ans = [k+a for a in arr]
    return ans