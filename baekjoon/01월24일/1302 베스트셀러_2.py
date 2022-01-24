import sys

d = dict()
# 1. 책 제목과 팔린 횟수 넣기
for _ in range(int(input())):
    book = input()
    # 1. 책제목이 존재하면 딕셔너리 값 1씩 증가
    if book in d:
        d[book] += 1
    # 2. 책제목 없으면 새로 추가
    else:
        d[book] = 1
# print(d.keys()) #키만 반환
# print(d.values()) #값만 반환
# print(d.items()) # (키, 값) 반환

# 2. 가장 많이 팔린 책 구하기
m = max(d.values()) #가장 많이 팔린책의 횟수
candi = []
for k, v in d.items():
    # print(k, v)
    if v == m: #가장많이 팔린 책의 횟수(값)와 같을 때
        candi.append(k) #키(책제목) 넣기

candi.sort() #오름차순 정렬
print(candi[0])