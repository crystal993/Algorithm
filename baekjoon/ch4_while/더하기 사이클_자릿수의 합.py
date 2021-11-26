# 파이썬으로 꼼수 쓰려고 하니깐 어려웠음.
# 이런 방식으로 풀면 편함.
#  자릿수의 합 문제 

import sys

input_num = int(sys.stdin.readline())

num = input_num
cnt = 0
while True:
    sum_num = (num // 10) + (num % 10) #각 자릿수를 더한 수
    new_num = ((num % 10) * 10) + (sum_num % 10)  #새로 만들어지는 수
    cnt += 1 #사이클 카운트
    if new_num == input_num :
        break
    num = new_num
print(cnt)
