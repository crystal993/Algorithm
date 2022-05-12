# 조합
# 서로 다른 n개에서 순서에 상관없이 서로 다른 r개를 선택하는 것
from itertools import combinations

data = ['A','B','C']

result = list(combinations(data, 2)) # 2개를 뽑는 모든 조합 구하기

# [('A', 'B'), ('A', 'C'), ('B', 'C')]
print(result)

# 중복 조합
from itertools import combinations_with_replacement

data = ['A','B','C']

result = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기 (중복 허용)

# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
print(result)