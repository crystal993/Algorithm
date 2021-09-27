import sys
sys.stdin = open("input.txt","rt")

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

sum = 0
sidx = fidx = hlen = int(n/2)
for i in range(n):
    for j in range(sidx, fidx+1):
        sum += data[i][j]
    if i < hlen:
        sidx -= 1
        fidx += 1
    else:
        sidx += 1
        fidx -= 1
print(sum)
