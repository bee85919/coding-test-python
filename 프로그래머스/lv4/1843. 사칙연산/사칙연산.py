def cal(a,b,c): return a+b if c=="+" else a-b

def solution(arr):    
    
    M, m, num, op = {}, {}, [int(x) for x in arr[::2]], [x for x in arr[1::2]]
    
    for i in range(len(num)): M[(i,i)], m[(i,i)] = num[i], num[i]
    
    for d in range(1,len(num)):
        for i in range(len(num)):
            j = d+i
            if j >= len(num): continue
            
            M_list, m_list = [], []
            for k in range(i+1, j+1):
                M_list.append(cal(M[(i,k-1)], m[(k,j)], op[k-1]))
                m_list.append(cal(m[(i,k-1)], M[(k,j)], op[k-1]))
            
            M[(i,j)], m[(i,j)] = max(M_list), min(m_list)
            
    return M[(0,len(num)-1)]