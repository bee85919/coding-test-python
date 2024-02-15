def solution(numbers):
    nums=list(map(str,numbers))
    temp=sorted(nums,key=lambda x:x*3,reverse=True)
    return str(int(''.join(temp)))