import sys

# 시간 256ms
def solve(a:list) -> int :
    for i in range(len(a)):
        sum += a[i]
    return sum

# 간단한 버전 56ms
def solve(a):
    ans = sum(a)
    return ans