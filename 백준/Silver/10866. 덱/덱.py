from collections import deque
import sys

N, DQ = int(sys.stdin.readline()), deque()
for _ in range(N):
    I = sys.stdin.readline().split()
    
    if I[0] == "push_front": DQ.appendleft(I[1])        
    elif I[0] == "push_back": DQ.append(I[1])        
    elif I[0] == "pop_front": print(DQ.popleft() if DQ else -1)        
    elif I[0] == "pop_back": print(DQ.pop() if DQ else -1)        
    elif I[0] == "size": print(len(DQ))        
    elif I[0] == "empty": print(1 if not DQ else 0)        
    elif I[0] == "front": print(DQ[0] if DQ else -1)        
    elif I[0] == "back": print(DQ[-1] if DQ else -1)     
