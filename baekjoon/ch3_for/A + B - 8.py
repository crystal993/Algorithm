# import sys
#
# T = sys.stdin.readline().rstrip()
# T = int(T)
#
# for x in range(1,T+1):
#     a, b = map(int, input().split())
#     print("Case #",x,": ",a," + ",b," = ",a+b)

import sys

T = sys.stdin.readline().rstrip()
T = int(T)

for x in range(1,T+1):
    a, b = map(int, input().split())
    print(f"Case #{x}: {a} + {b} =",a+b)