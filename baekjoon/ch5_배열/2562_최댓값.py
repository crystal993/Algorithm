import sys

n_lst = []
max = -(sys.maxsize + 1) #최대값에는 int형 중에 제일 작은값 넣기!!
cnt = 0

for i in range(9):
    n = int(sys.stdin.readline())
    cnt += 1
    if n > max :
        max, max_idx = n, cnt
print(max)
print(max_idx)