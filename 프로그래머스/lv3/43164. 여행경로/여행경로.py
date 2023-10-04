def solution(tickets):
    
    routes = {}
    for t in sorted(tickets, reverse=True):
        if t[0] in routes:
            routes[t[0]].append(t[1])
        else:
            routes[t[0]] = [t[1]]
            
    stack = ["ICN"]
    path = []

    while stack:
        top = stack[-1]
        if top in routes and routes[top]:
            stack.append(routes[top].pop())
        else:
            path.append(stack.pop())

    return path[::-1]