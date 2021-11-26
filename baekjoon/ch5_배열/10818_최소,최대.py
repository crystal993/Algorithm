import sys

n = int(sys.stdin.readline())
n_lst = list(map(int, sys.stdin.readline().split()))

# min = sys.maxsize #최소값에 최대값 저장
# max = -(sys.maxsize + 1) #최대값에 최소값 저장

#이게 더 빠름
min = sys.maxsize #최소값에 최대값 저장
max = n_lst[0] #최대값에 최소값 저장

for i in range(len(n_lst)):
    if n_lst[i] < min :
        min = n_lst[i]
    if n_lst[i] > max :
        max = n_lst[i]
print(min,max)