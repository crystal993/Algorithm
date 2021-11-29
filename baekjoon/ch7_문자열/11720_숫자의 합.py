import sys
n = int(sys.stdin.readline().rstrip())
m = list(str(sys.stdin.readline().rstrip()))
sum = 0
for i in m:
    sum += int(i)
print(sum)
