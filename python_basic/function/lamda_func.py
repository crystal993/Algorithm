# ------- 람다표현식 -------
def add(a,b):
    return a + b

# 일반적인 add() 메서드 사용
print(add(3,7))

# 람다 표현식으로 구현한 add() 메서드
print((lambda a,b: a + b)(3,7))

# 내장 함수에서 자주 사용되는 람다 함수
array = [('홍길동', 50),('이순신', 32),('아무개', 74)]

def my_key(x):
    return x[1]

print(sorted(array, key=my_key))
print(sorted(array, key=lambda x:x[1]))

# 여러 개의 리스트에 적용
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

result = map(lambda a,b:a+b,list1,list2)
print(list(result))
