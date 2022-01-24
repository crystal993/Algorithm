import sys

m = {}
today = []
# 1. 제목 리스트 만들기
for _ in range(int(input())):
    today.append(input())
# 2. 딕셔너리 key에 중복제거한 키 값 넣기
for i in list(set(today)):
    m[i] = 0
# 3. 제목 횟수 세기
for i in today:
    if i in m :
        m[i] += 1
# 가장 큰 값을 가진 key(책 제목) 출력
n = sorted(m.items(), key=lambda x: x[1])
print(n[-1][0])
