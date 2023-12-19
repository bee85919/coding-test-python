def function(arr):
    n = len(arr)
    for i in range(n):
        ai = arr[i]
        if ai >= 50 and ai%2 == 0: arr[i] //= 2
        if arr[i] < 50 and arr[i]%2 == 1:
            arr[i] = arr[i]*2 + 1
    return arr

def solution(arr):
    cnt = 0
    while True:
        _arr = arr[:]
        arr = function(arr)
        if _arr == arr:
            return cnt
        cnt += 1
            