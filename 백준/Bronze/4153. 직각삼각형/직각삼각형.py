i = -1
while True:
    i += 1    
    a, b, c = sorted(map(int, input().split()))    
    if a == 0 and b == 0 and c == 0: break    
    print('right') if a**2 + b**2 == c**2 else print('wrong')   