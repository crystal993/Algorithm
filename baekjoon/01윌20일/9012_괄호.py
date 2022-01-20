import sys
from collections import deque

n = int(input())

for _ in range(n):
	s = []
	isVps = True

	for i in input():
		if i == '(': #(이 있으면
			s.append('(') #스택에 넣기
		else : # )이라면
			if s :
				s.pop() # 아까넣은 ( 빼기
			else : #스택에 없는데 또 빼야하는경우(짝이 안 맞음)
				isVps = False
				break

	if s: #스택에 (가 남아있으면
		isVps = False #false

	if isVps:
		print("YES")
	else :
		print("NO")