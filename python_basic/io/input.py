# ==== 입력을 위한 코드1 ====
# 데이터의 개수 입력
n = int(input())

# 각 데이터를 공백을 기준으로 구분하여 입력
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)

# ==== 입력을 위한 코드2 ====
# n,m,k를 공백을 기준으로 구분하여 입력한다. 
n, m, k = map(int, input().split())
print(n, m, k)