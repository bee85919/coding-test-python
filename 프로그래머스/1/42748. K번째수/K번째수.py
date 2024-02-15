def solution(arr, cmd):
    return [sorted(arr[i-1:j])[k-1] for i,j,k in cmd]