T = int(input())

for _ in range(T):
    R, S = input().split()
    ans = ""
    for s in S:
        ans += s * int(R)
    print(ans)