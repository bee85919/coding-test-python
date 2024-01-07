n = int(input())
card = list(map(int, input().split(" ")))
m = int(input())
nums = list(map(int, input().split(" ")))


di = {}
for i in range(n):
    di[card[i]] = 0

    
for j in range(m):
    if nums[j] not in di:
        print(0, end = ' ')
    else:
        print(1, end = ' ')