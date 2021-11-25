import sys
sys.stdin=open("input.txt", "r")

N = int(input())
num = list(map(int, input().split()))

print(num)

# 1단계 : 예를 들어 125를 1,2,5로 분리하기
str_list = []
for n in num:
    str_list.append(list(str(n)))

print(str_list)


# 2단계 : 각 자리수 문자열을 int타입으로 만들어서 더한 값을 다시 sum_list에 넣어주기
sum_list=[]
sum = 0
for num_list in str_list:
    sum = 0
    for n in num_list:
        sum += int(n)
    sum_list.append(sum)

# print(num)
print(sum_list)

# 3단계 : 자릿수의 합 중에 최대값 구하기
max = 0 #최대값 구할 변수
midx = 0
for idx, i in enumerate(sum_list):
    if i > max:
        max=i
        midx=idx

print(num[midx])

