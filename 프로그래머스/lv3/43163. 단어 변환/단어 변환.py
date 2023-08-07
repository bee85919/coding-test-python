from collections import deque


def diff(word1, word2): 
    return sum(1 for a, b in zip(word1, word2) if a != b)


def solution(begin, target, words):
    
    if target not in words: return 0
    
    visit, queue = set(), deque([(begin, 0)])
    
    while queue:        
        que, depth = queue.popleft()        
        if que == target: 
            return depth
        
        for word in words:
            if word not in visit and diff(que, word) == 1:
                visit.add(word)
                queue.append((word, depth+1))
                
    return 0