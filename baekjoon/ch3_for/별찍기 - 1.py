import sys

n = int(sys.stdin.readline())
star = ''

# 개행 있는 버전
for i in range(n):
    star = star + '*'
    print(star)
