import sys
sys.stdin=open("in3.txt","r")

# 1단계 : 1 ~ 20 까지 카드 생성
card=[]
for i in range(1,21):
    card.append(i)

for _ in range(10):
    # for문 돌아갈때마다 초기화
    section=[] 
    section = list(map(int, input().split()))

    # 2단계 : 카드 [5, 6, 7, 8, 9, 10] 리스트에 저장
    sub = list(card[section[0]-1:section[1]])
    # print(sub)
    # print(section[0]-1,section[1]) # 실제 카드 위치

    # 3단계 : [5, 6, 7, 8, 9, 10] 해당되는 값 삭제
    for i in sub:
        card.remove(i)
        # print(card)

    # 4단계 : sub리스트 맨 뒤에 값 삭제, i위치에 값 삽입
    # [ 5,6,7, 8, 9, 10]
    for i in range(section[0]-1,section[1]):
        n = sub.pop()
        # print(n)
        card.insert(i,n)

for i in card:
    print(i,end=' ')