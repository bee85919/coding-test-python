def cal(a,b,op): return a+b if op=="+" else a-b

def solution(arr):    
    
    M, m, num, ops = {}, {}, [int(x) for x in arr[::2]], [x for x in arr[1::2]]
    
    for i in range(len(num)): M[(i,i)], m[(i,i)] = num[i], num[i]
    
    for d in range(1,len(num)):
        for i in range(len(num)):
            if i+d >= len(num): continue
            
            M_list, m_list = [], []
            for k in range(i+1, i+1+d):
                M_list.append(cal(M[(i,k-1)], m[(k,i+d)], ops[k-1]))
                m_list.append(cal(m[(i,k-1)], M[(k,i+d)], ops[k-1]))
            
            M[(i,i+d)], m[(i,i+d)] = max(M_list), min(m_list)
            
    return M[(0,len(num)-1)]