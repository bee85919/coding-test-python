from functools import reduce


def solution(num_list):
    cal1 = reduce(lambda x,y: x*y, num_list)
    cal2 = sum(num_list)**2
    return 1 if cal1 < cal2 else 0