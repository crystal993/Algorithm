# --------- for문 ---------

# 리스트 방문
array = [9,8,7,6,5]

for x in array:
    print(x, end=" ")

print()
# 튜플 방문
array2 = (9,8,7,6,5)

for x in array2:
    print(x, end=" ")

# ---------- range() -----------
result = 0

# i는 1부터 9까지의 모든 값을 순회
for i in range(1,10):
    result += i
print('\n',result)

# ----- continue 키워드 -----
result = 0

# 홀수의 합
for i in range(1,10):
    if i % 2 == 0:
        continue
    result += i
print(result)

# ----- break 키워드 -----
i = 1

while True:
    print("현재 i의 값:", i)
    if i == 5:
        break
    i += 1
