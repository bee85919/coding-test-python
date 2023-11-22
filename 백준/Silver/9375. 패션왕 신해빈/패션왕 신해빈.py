t = int(input())


for _ in range(t):
    n = int(input())
    clothes = {}
    for _ in range(n):
        _, category = input().split()
        if category in clothes:
            clothes[category] += 1
        else:
            clothes[category] = 1


    result = 1
    for key in clothes:
        result *= (clothes[key] + 1)


    print(result - 1)