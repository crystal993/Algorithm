import sys
sys.stdin=open("in1_1.txt", "r")
n = int(input())
num = list(map(int,input().split()))

# isDegit()원리 
def reverse(x): # 32
    s = 0
    res = 0
    while x > 0:
        s = x % 10   # s = 32 % 10 = 2, s = 3
        res = res * 10 + s # res = 2 , res = 2 * 10 +3
        x = x // 10 # 32의 몫 : 3  , x = 0
    return res # 23

# 소수: 1과 자기자신만 약수(0으로 나누어떨어짐)로 갖는 수 -> 2개
def isPrime(x):
    cnt = 0
    for i in range(1, x+1):
        if x % i == 0:
            cnt += 1

    if cnt == 2:
        return True
    else:
        return False

for n in num:
    m = reverse(n)
    if isPrime(m) :
        print(m, end=' ')




