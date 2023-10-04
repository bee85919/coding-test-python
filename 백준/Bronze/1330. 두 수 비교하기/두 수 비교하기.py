a, b = map(int, input().split())
if a > b:
    answer = '>'
if a < b:
    answer = '<'    
if a == b:
    answer = '=='
print(answer)