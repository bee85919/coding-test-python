def F(n): return 1 if n==0 else n*F(n-1)

N = str(F(int(input())))

cnt = 0
for i in range(-1, -len(N)-1, -1):
    if N[i] != '0':
        break
    else:
        cnt +=1

print(cnt)