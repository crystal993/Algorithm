# ========= 리스트 컴프리헨션 ==========
# 리스트를 초기화하는 방법 중 하나
array = [i for i in range(10)]
print(array)

# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 ==1]
print(array)

# 1부터 9까지의 수들의 제곱값을 포함하는 리스트
array = [i*i for i in range(1,10)]
print(array)

# ========= 2차원리스트 초기화 ===========
n = 3
m = 4
array = [[0]*m for _ in range(n)]
print(array)
