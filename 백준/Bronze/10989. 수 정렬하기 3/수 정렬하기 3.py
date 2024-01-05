import sys
input = sys.stdin.readline


n = int(input())


cnt_list = [0] * 10001
for _ in range(n):
    num = int(input())
    cnt_list[num] += 1


for num in range(10001):
    if cnt_list[num] != 0:
        for cnt in range(cnt_list[num]):
            print(num)