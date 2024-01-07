n = int(input())
card = set(map(int, input().split(" ")))
m = int(input())
nums = list(map(int, input().split(" ")))


for j in range(m):
    if nums[j] not in card:
        print(0, end = ' ')
    else:
        print(1, end = ' ')