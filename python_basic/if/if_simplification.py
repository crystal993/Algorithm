# ------ 조건문의 간소화 ------
score = 85

# 조건문에서 실행될 코드가 한줄일 때, 줄바꿈을 하지 않아도 된다.
if score >= 80: result = "Success"
else: result = "Fail"
print(result)

# 한줄에 작성하는 것이 가능하다.
result = "Success" if score >= 80 else "Fail"
print(result)