num = [int(input()) for _ in range(10)]
print(len({n % 42 for n in num}))