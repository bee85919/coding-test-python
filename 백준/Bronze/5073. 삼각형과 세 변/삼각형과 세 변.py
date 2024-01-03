while True:
    A, B, C = sorted(list(map(int, input().split(" "))))
    if A == B == C == 0:
        break
    elif A + B <= C:
        print("Invalid")
    elif A == B and B == C:
        print("Equilateral")
    elif A == B or B == C or C == A:
        print("Isosceles")
    elif A != B and B != C and C != A:
        print("Scalene")