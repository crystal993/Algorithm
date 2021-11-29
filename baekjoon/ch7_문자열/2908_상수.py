import sys

x,y = map(str, sys.stdin.readline().split())
x = x[::-1]
y = y[::-1]

# 이 과정 for문 없어도 됨
new_x, new_y = '', ''
for i in range(len(x)):
    new_x += x[i]
    new_y += y[i]

if int(new_x) > int(new_y):
    print(new_x)
else:
    print(new_y)

