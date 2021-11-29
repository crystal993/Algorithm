import sys

x,y = map(str, sys.stdin.readline().split())
x = x[::-1]
y = y[::-1]

if int(x) > int(y):
    print(x)
else:
    print(y)

