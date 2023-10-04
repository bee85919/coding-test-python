year = int(input())

cond1 = (year%4==0)
cond2 = (year%100!=0) or (year%400==0)

if cond1 and cond2:
    print(1)
else:
    print(0)