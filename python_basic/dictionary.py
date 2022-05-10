# 사전 자료형은 특정 키가 존재하는지 검색하는데에
# 상수시간이 소요가 된다.

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")

#  키 데이터만 담은 리스트
key_list = data.keys();

# 값 데이터만 담은 리스트
value_list = data.values();

print(key_list) # 키 리스트 출력
print(value_list) # 값 리스트 출력

# 각 키에 따른 값을 하나씩 출력
for key in key_list:
    print(data[key])

a = dict()
a['홍길동'] = 97
a['이순신'] = 98
print(a)

b = {
    '홍길동' : 97,
    '이순신' : 98
}
print(b)

key_list = b.keys()
print(key_list)
