import sys # 23분
sys.stdin=open("input.txt", "r")

# 0단계 : 문자열 문자로 개별씩 저장
words = list(str(input()))
print(words)

# 아스키코드값 확인 ord()
# 0 : 48 ~ 57
# a ~ z : 97 ~ 122 len(25)
# print(ord('a'),ord('z'))
# A ~ Z : 65 ~ 90
# print(ord('A'),ord('Z'))

# 1단계 : 문자 문자열과 숫자 문자열 분리
num = []
for w in words:
    if ord('0') <= ord(w) <= ord('9'):
        num.append(w)
        # 맨 앞이 0이면
        if num[0] == '0':
            num.pop(0) #맨 앞인덱스 제거
print(num)

# 2단계 : 자리 합 구하기 28
# num[0]  sum +=  2 * (10^1)
# num[1]  sum +=  8 * (10^0)
sum = 0
for i in range(len(num)):
    sum += int(num[i]) * (10 ** (len(num)-i-1))


# 3단계 : 약수 갯수 구하기
cnt = 0
for i in range(1,sum+1):
    if sum % i == 0 :
        cnt += 1

print(sum)
print(cnt)

