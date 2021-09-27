import sys
sys.stdin = open("input.txt", "r")

# 0단계 : 입력값 받기, data부분 2중리스트로 미리 초기화하는 부분 중요 
n = int(input())
data = [ list(map(int, input().split())) for _ in range(n)]
# print(data)

# 1단계 : 각 행의 합, 각 열의 합, 각 대각선의 합 리스트에 넣기
sum_lst = []
d_sum1, d_sum2 = 0, 0
for i in range(n):

    col_sum , row_sum = 0, 0
    d_sum1 += data[i][i] #왼쪽 대각선의 합 
    d_sum2 += data[i][n-1-i] #오른쪽 대각선의 합

    for j in range(n):
        col_sum += data[j][i] #열의 합 , 미리 초기화 해둬야 여기서 접근 가능
        row_sum += data[i][j] #행의 합

    sum_lst.append(row_sum) # sum_lst.append(sum(data[i]))
    sum_lst.append(col_sum)
sum_lst.append(d_sum1)
sum_lst.append(d_sum2)

print(data)
print(sum_lst)

# 2단계: 최대값 구하기  - 방법1 >  메서드 이용 1
print(max(sum_lst))

# 2단계: 최대값 구하기  - 방법2 > 직접
max = 0
for i in sum_lst:
    if max < i:
        max = i
print(max)