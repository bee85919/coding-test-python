import heapq as hq


def solution(operations):
    heap=[]
    for operation in operations:
        if operation[0]=='I':
            _,num=operation.split()
            hq.heappush(heap,int(num))
        elif operation=='D 1' and heap:
            heap.pop(heap.index(max(heap)))
        elif operation=='D -1' and heap:
            hq.heappop(heap)
    
    if heap:
        return [max(heap),min(heap)]
    else:
        return [0,0]
