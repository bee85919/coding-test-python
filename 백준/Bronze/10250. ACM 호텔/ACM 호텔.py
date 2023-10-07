T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    
    f_num = N % H
    r_num = N // H + 1
    
    if f_num == 0:
        f_num = H
        r_num -= 1
    print(f_num*100 + r_num)