import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
gob = a*b*c
n_lst = list(str(gob))

for i in range(10):
    cnt = 0
    for n in n_lst:
        if i == int(n):
            cnt += 1
    print(cnt)

