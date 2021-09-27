import sys #시간 초과
sys.stdin=open("in1_2.txt","r")

N = int(input())

sosu_cnt = 0
cnt = 0
for n in range(1, N + 1):
    sosu_cnt = 0
    for j in range(1, n + 1):
        if n % j == 0:  # 소수는 자기자신과 1만 가지니깐 sosu_cnt는 무조건 2가 되어야함
            sosu_cnt += 1

    if sosu_cnt == 2:
        cnt += 1
print(cnt)