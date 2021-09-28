import sys
sys.stdin = open("input.txt","rt")

n = int(input())
n_data = [list(map(int, input().split())) for _ in range(n)]
rotate = int(input())
r_data = [list(map(int, input().split())) for _ in range(rotate)]

# 1단계 : 회전 실행하는 갯수만큼 for문 돌림.
for i in range(rotate):
    for j in range(r_data[i][2]):
        tmp = 0
        # 왼쪽
        if r_data[i][1] == 0:
           tmp = n_data[r_data[i][0]-1].pop(0)
           n_data[r_data[i][0]-1].append(tmp)
           # n_data[r_data[i][0] - 1]
        # 오른쪽
        else :
            tmp = n_data[r_data[i][0]-1].pop()
            n_data[r_data[i][0]-1].insert(0, tmp)
            # n_data[r_data[i][0] - 1]

# print(n_data)
sum = 0
hlen = int(n/2)
sidx, fidx = 0, n
for i in range(n):
    for j in range(sidx, fidx):
        # print(n_data[i][j] , i, j)
        sum += n_data[i][j]
    if i >= hlen:
        sidx -= 1
        fidx += 1
    else:
        sidx += 1
        fidx -= 1
    # print(i,'번째 줄 합:',sum)


print(sum)


