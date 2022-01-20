# 	1. N만큼 큐에 담는다
# 	2. 맨 앞에 거 버리기
# 	3. 그다음 버릴거 변수에 저장하고 다시 맨 뒤에 추가
# 	4. 2,3번 반복 queue의 길이가 1이될때까지
#   5. 길이가 1이면 최종 카드 반환
from collections import deque

n = int(input())
# dq = deque()
#
# for i in range(1,n+1):
#     dq.append(i)
dq = deque(range(1,n+1)) #위에 주석처리한 부분과 같음.

while len(dq) > 1 :
    dq.popleft() #큐의 맨 처음거 버림 
    next = dq.popleft() #큐의 그 다음거 저장
    dq.append(next) #큐 맨뒤로 옮김

print(dq[0])


