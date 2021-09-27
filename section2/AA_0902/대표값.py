# N = int(input())
# num = list(map(int, input().split()))
# import math
N = 10
num = [45,73,66,87,92,67,75,79,75,80]

sum = 0
# 합 구하기
for n in num:
    sum += n

# 평균 구하기 - 반올림해야함
avg = round(sum / len(num))

min=float('inf')
for idx, n in enumerate(num):
    dis = abs(n-avg)
    if dis < min:
        min=dis
        score=n  # 제일 차이가 작은 학생점수
        min_idx=idx+1 # 제일 차이가 작은 인덱스

    elif dis == min:
        if n > score:
            score=n
            min_idx=idx+1

print(avg,min_idx)



