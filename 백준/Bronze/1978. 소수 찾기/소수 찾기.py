N = int(input())
Set = set(map(int,input().split()))
P = 0
for S in Set:
    check = 0
    if S > 1:
        for i in range(2,S):
            if S % i == 0:
                check = 1
                break
        if check == 0:
            P += 1
print(P)