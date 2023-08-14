def solution(arr, query):
    for i, que in enumerate(query):
        if i%2 == 0: 
            arr = arr[:que+1]
        else: 
            arr = arr[que:]
    return arr