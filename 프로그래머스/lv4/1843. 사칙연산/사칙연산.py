def cal(a,b,op): return a+b if op=="+" else a-b


def solution(arr):    

    M, m, num, ops = {}, {}, [int(x) for x in arr[::2]], [x for x in arr[1::2]]

    for i in range(len(num)): M[(i,i)], m[(i,i)] = num[i], num[i]
    
    for d in range(1,len(num)):
        for i in range(len(num)-d):  
            
            M_list, m_list = [cal(M[(i,k)], m[(k+1, i+d)], ops[k]) for k in range(i, i+d)], [cal(m[(i,k)], M[(k+1, i+d)], ops[k]) for k in range(i, i+d)]
                
            M[(i, i+d)], m[(i, i+d)] = max(M_list), min(m_list)
            
    return M[(0,len(num)-1)]
