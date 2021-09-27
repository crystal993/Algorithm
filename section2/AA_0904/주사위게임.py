import sys
sys.stdin=open("in1_2.txt","r")

N = int(input())

price_list = [] # 가격을 담을 리스트 변수
dice = [] # 주사위 눈을 담을 리스트 변수

# 1단계: 참여하는 사람의 수 N만큼 주사위를 돌려야한다.
for n in range(N):
    dice = list(map(int, input().split())) # [3 3 6]
    print(dice)

    cnt = 0 # 같은 수의 눈이 몇개 있는지 카운팅하는 변수
    next = dice[0]
    next_idx = 0

    # 2단계 : [3, 3, 6] 리스트 내에서 같은 수 카운팅 (최대값,최소값과 원리 같음)
    for idx, i in enumerate(dice):
            if i == next:
                next = i 
                cnt += 1
                next_idx = idx
    print(cnt)
    print(next_idx)

    # 3단계 : 같은 수의 눈이 2개, 3개, 없느냐에 따라 가격이 다름.
    if cnt == 2 :
        price = 1000 + dice[next_idx] * 100
    elif cnt == 3:
        price = 10000 + dice[next_idx] * 1000
    else: #없을 때 => 가장 큰 눈을 기준으로 가격 책정(최대값 구하기)
        cnt = 0
        max = 0 #최대값
        for idx, i in enumerate(dice):
            if i > max:
                max = i
                cnt += 1
        price = max * 100

    price_list.append(price) # 가격을 price_list에 저장
    print(price_list)


# 4단계 : N번만큼 주사위를 돌리면서 price_list에 저장된 가격들 
# 중에서 가장 높은 가격을 구하기 (최대값 구하기)
for i in price_list:
    if i > max:
        max = i

print(max)