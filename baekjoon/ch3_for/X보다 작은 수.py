import sys

N, X = map(int, sys.stdin.readline().split())
nums = list(sys.stdin.readline().split())

for i in range(N):
    if int(nums[i]) < X:
        print(nums[i],end=' ')