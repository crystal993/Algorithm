import sys

n = int(sys.stdin.readline())
pre_scores = list(map(int, sys.stdin.readline().split()))
new_scores = [0]*len(pre_scores)

M = max(pre_scores)

for i in range(len(pre_scores)):
    new_scores[i] = (pre_scores[i] / M )* 100
new_avg = sum(new_scores)/n
print(new_avg)