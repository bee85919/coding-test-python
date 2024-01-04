n = int(input())
cnt = 9999
idx3 = n//3
idx5 = n//5
for i3 in range(0, idx3+1):
    for i5 in range(0, idx5+1):
        if n == i3*3 + i5*5:
            cnt = min(cnt, i3+i5)
print(cnt if cnt != 9999 else -1)