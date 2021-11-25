import sys
sys.stdin=open("input.txt", "r")
N, M = map(int, input().split())


sum = [] #주사위 눈의 합을 담을 리스트 
sum_cnt_list = [0]*(N+M-1) #주사위 눈의 합 카운팅할 거 담을 리스트
# print(idx_list)


# 1단계 : sum 리스트에 주사위 눈의 합을 넣어 준다.
for i in range(1, N+1) :
    for j in range(1, M+1):
        s = i + j
        sum.append(s)

print(sum)

# 2단계 : sum2리스트에 중복제거한 주사위 합의 값을 넣는다. (set이용)
sum2 = list(set(sum)) # 중복제거한 sum

print(sum2)

# 3단계 : sum2만큼 돌리고 중복제거하지 않은 sum과 비교해서 같으면 카운팅을 1로 올려준다.
# sum_cnt_list 에 합의 확률이 들어가게 된다.
for idx, n in enumerate(sum2):
    for s in sum:
        if n == s:
            sum_cnt_list[idx] += 1

# print(sum)
# print(sum2)
print(sum_cnt_list)

max = 0 #최대값 구할 때 제일 작은 값
max_list = []
midx = 0
# sum_cnt_list 인덱스를 이용하는 게 핵심
# sum_cnt_list와 sum2의 인덱스는 같음
# 4단계 : sum2에서 가장 확률이 높은 숫자 구하기 (최대값 구하기)
for idx, i in enumerate(sum_cnt_list):
    if max < i : #최대값 구하기
        print(max, '<', i)
        max = i   # sum_cnt_list와 최대값을 저장
        midx = idx # midx는 idx_list의 최대값의 인덱스 저장
    elif max == i :
        max_list.append(sum2[idx])

max_list.append(sum2[midx])
max_list.sort()  #오름차순으로 정렬 
# print('max:',max,'midx:',midx)
# print(max_list)

for i in max_list:
    print(i, end=' ')




