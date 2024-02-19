import heapq as hq


def solution(jobs):
    jobs.sort()
    print(jobs)
    n=len(jobs) 
    
    time=0
    time_sum=0  
    heap=[]    
    while jobs or heap:
        while jobs and jobs[0][0]<=time:
            start, duration=jobs.pop(0)
            hq.heappush(heap,(duration,start))    
        if heap:
            duration,start=hq.heappop(heap)
            time+=duration
            time_sum+=(time-start)
        else:
            time+=1       
    return time_sum//n
