from collections import Counter


def solution(participant, completion):
    dic = Counter(participant)
    
    for c in completion:
        dic[c] -= 1
        if dic[c] == 0:
            del dic[c]
    
    return list(dic.keys())[0]
