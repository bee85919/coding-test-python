def solution(num, n): 
		return 1 if not num and n == 0 else 0 if not num else solution(num[1:],n-num[0]) + solution(num[1:],n+num[0])