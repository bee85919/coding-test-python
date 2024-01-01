from collections import Counter


def solution(participant, completion):
    dic1 = Counter(participant)
    dic2 = Counter(completion)
    ans = dic1-dic2
    return list(ans.keys())[0]
