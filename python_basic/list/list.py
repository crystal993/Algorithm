### ========= 리스트 자료형 =========
#  직접 데이터를 넣어 초기화
a = [1,2,3,4,5,6,7,8,9]
print(a)

# 네번째 원소만 출력
print(a[3])

# 크기가 n이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n
print(a)

### ========= 인덱싱 =========
# 여덟 번째 원소만 출력
a = [1,2,3,4,5,6,7,8,9]
print(a[7])

# 뒤에서 첫번째 원소 출력
print(a[-1])

# 뒤에서 세번째 원소 출력
print(a[-3])

# 네번째 원소 값 변경
a[3] = 7
print(a)

# ========= 슬라이싱 ==========
a = [1,2,3,4,5,6,7,8,9]

# 네번째 원소만 출력
print(a[3])

# 두번째 원소부터 네번째 원소까지
print(a[1:4])

