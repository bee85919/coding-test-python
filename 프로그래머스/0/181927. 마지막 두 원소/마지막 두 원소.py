def solution(li):
    num1 = int(li[-1])
    num2 = int(li[-2])
    num = num1 - num2 if num1 > num2 else num1 * 2
    li.append(num)
    return li