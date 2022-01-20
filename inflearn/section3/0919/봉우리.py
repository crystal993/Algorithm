import sys
sys.stdin = open("input2.txt", "r")

n = int(input())

# 1단계 : 초기화 하기
datas = [[0]*(n+2)]
data = []
for i in range(n):
    data = list(map(int, input().split()))
    data.insert(0, 0)
    data.insert(n+1, 0)
    datas.append(data)

datas.append([0]*(n+2))
# print(datas)

# 2단계 : 봉우리 갯수 구하기
m_cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if datas[i][j] > datas[i][j-1] and datas[i][j] > datas[i][j+1] and  datas[i][j] > datas[i-1][j] and datas[i][j] > datas[i+1][j]:
            m_cnt += 1


print(m_cnt)