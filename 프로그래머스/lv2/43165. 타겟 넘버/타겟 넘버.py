def solution(num, target):
    dic = {0 : 1}
    for n in num:
        temp = {}
        for val, cnt in dic.items():
            temp[val+n] = temp.get(val+n, 0) + cnt
            temp[val-n] = temp.get(val-n, 0) + cnt
        dic = temp
    return dic.get(target, 0)