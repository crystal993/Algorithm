# 조금 특이한 문제
# 각 자리의 차이가 0인 경우는 포함 x
# 1자리수, 2자리 수들은 모두 한수가 된다.
# 3자리 수부터 한수 계산
# def solve(a):

import sys

n = int(sys.stdin.readline())
cnt = 0
for i in range(1,n+1):
    if i < 100:
        cnt += 1
    else:
        num = list(str(i))
        if int(num[0]) - int(num[1]) == int(num[1]) - int(num[2]):
            cnt += 1
print(cnt)



# 함수 형태
# def solve(a):
#     cnt = 0
#     for i in range(1,a+1):
#         if i < 100:
#             cnt += 1
#         else:
#             num = list(str(i))
#             if int(num[0]) - int(num[1]) == int(num[1]) - int(num[2]):
#                 cnt += 1
#     return cnt
#
# import sys
# n = int(sys.stdin.readline())
# print(solve(n))