import sys
# sys.stdin=open("input.txt","r")
n,k=map(int, input().split())

num=[]
cnt=0
for i in range(1,n+1):
    if n % i == 0:
        num.append(i)
        cnt += 1
        # num.sort()

if cnt >= k:
    print(num[k - 1])
else:
    print(-1)


