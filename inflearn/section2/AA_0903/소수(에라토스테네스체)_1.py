import sys
sys.stdin=open("in1_2.txt", "r")

n = int(input())
ch = [0]*(n+1)
cnt = 0
for i in range(2,n+1):
    if ch[i] == 0 :
        cnt += 1
        for j in range(i, n+1, i): #i의 배수에 step=i만큼 증가
            ch[j]=1
print(cnt)


