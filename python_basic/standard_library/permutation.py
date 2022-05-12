# 순열
# 서로 다른 n개 에서 서로 다른 r개를 선택하여 일렬로 나열하는 것
from itertools import permutations

data = ['A','B','C'] # 데이터 준비

result = list(permutations(data,3)) #모든 순열 구하기

# [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
print(result)

# 중복 순열
from itertools import product

data = ['A','B','C']

result = list(product(data, repeat=2)) #2개를 뽑는 모든 순열 구하기 (중복 허용)

# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
print(result)
