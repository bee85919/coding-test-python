from collections import defaultdict


def dfs(node,par,g): # par=parent
    nodes={node}
    for nbr in g[node]: # nbr=neighbor
        if nbr!=par: 
            nodes|=dfs(nbr,node,g) # update nodes
    return nodes


def graph(wire):
    g=defaultdict(set)    
    for w1,w2 in wire: 
        g[w1].add(w2) # key = node
        g[w2].add(w1) # val = nbr
    return g


def brute(wire,g):
    diff=[]
    for w1,w2 in wire:
        l1=len(dfs(w1,w2,g))
        l2=len(dfs(w2,w1,g))
        diff.append(abs(l1-l2))
    return diff

    
def solution(n,wire):
    g=graph(wire) # get nbr nodes
    diff=brute(wire,g) # brute force        
    return min(diff)