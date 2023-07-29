def solution(str1,str2):
    result=''
    for s1,s2 in zip(str1,str2): result+=s1+s2
    return result